import os
import base64
from pathlib import Path
import yaml
from openai import OpenAI

def load_manifest(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def build_prompt(item: dict, global_negative: str = "") -> str:
    p = item["prompt"].strip()
    neg = item.get("negative_prompt", "").strip()
    parts = [p]
    # Merge “negative prompts” as explicit constraints inside the prompt text
    avoid_bits = [x for x in [global_negative, neg] if x]
    if avoid_bits:
        parts.append("\n\nConstraints (avoid): " + " | ".join(avoid_bits))
    return "".join(parts)

def main():
    manifest_path = Path("art/manifest.yaml")
    out_dir = Path("art/renders")
    out_dir.mkdir(parents=True, exist_ok=True)

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set. Export it in your shell first.")

    manifest = load_manifest(manifest_path)
    g = manifest.get("global", {})
    global_negative = g.get("global_negative", "")

    client = OpenAI()

    for item in manifest["images"]:
        filename = item["filename"]
        out_path = out_dir / filename

        # Skip if already generated (handy for iterative runs)
        if out_path.exists():
            print(f"Skipping (exists): {filename}")
            continue

        model = item.get("model", g.get("model", "gpt-image-1.5"))
        size = item.get("size", g.get("size", "1536x1024"))
        quality = item.get("quality", g.get("quality", "auto"))
        output_format = item.get("output_format", g.get("output_format", "png"))

        prompt = build_prompt(item, global_negative)

        print(f"Generating {filename} | model={model} size={size} quality={quality} fmt={output_format}")

        img = client.images.generate(
            model=model,
            prompt=prompt,
            n=1,
            size=size,
            quality=quality,
            output_format=output_format,
        )

        image_bytes = base64.b64decode(img.data[0].b64_json)
        out_path.write_bytes(image_bytes)

        # Optional sidecar metadata for auditing/repro
        meta_path = out_dir / f"{Path(filename).stem}.meta.txt"
        meta_path.write_text(prompt, encoding="utf-8")

    print("Done. Outputs in art/renders/")

if __name__ == "__main__":
    main()
