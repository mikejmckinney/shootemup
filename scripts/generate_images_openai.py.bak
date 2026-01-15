import os, json, base64
from pathlib import Path
from openai import OpenAI

MANIFEST_PATH = "art/manifest.json"
OUT_DIR = Path("art/renders")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("Missing OPENAI_API_KEY env var.")

    client = OpenAI()

    manifest = json.loads(Path(MANIFEST_PATH).read_text(encoding="utf-8"))
    images = manifest["images"]

    for item in images:
        filename = item["filename"]
        prompt = item["prompt"]
        size = item.get("size", "1536x1024")  # landscape default
        model = item.get("model", "gpt-image-1.5")

        print(f"Generating {filename} ({size})...")
        img = client.images.generate(
            model=model,
            prompt=prompt,
            n=1,
            size=size
        )

        image_bytes = base64.b64decode(img.data[0].b64_json)
        (OUT_DIR / filename).write_bytes(image_bytes)

    print("Done. Images saved to art/renders/")

if __name__ == "__main__":
    main()
