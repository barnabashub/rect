import json
import os
import shutil

# Configuration
BUILD_DIR = "public"
REDIRECT_TEMPLATE = "redirect-template.html"
DATA_FILE = "redirects.json"
STATIC_FILES = ["index.html", "404.html"]

def build():
    # 1. Clean and create build directory
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR)

    # 2. Copy static UI files to build directory
    for file in STATIC_FILES:
        if os.path.exists(file):
            shutil.copy(file, os.path.join(BUILD_DIR, file))

    # 3. Load redirects
    with open(DATA_FILE, 'r') as f:
        redirects = json.load(f)

    with open(REDIRECT_TEMPLATE, 'r') as f:
        template = f.read()

    # 4. Generate redirect folders inside BUILD_DIR
    for slug, url in redirects.items():
        slug_path = os.path.join(BUILD_DIR, slug)
        os.makedirs(slug_path, exist_ok=True)
        with open(os.path.join(slug_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(template.replace("{{URL}}", url))
        print(f"✅ Generated: {BUILD_DIR}/{slug}/index.html")

if __name__ == "__main__":
    build()
