import json
import os

def generate_redirects():
    # Load the redirect data
    with open('redirects.json', 'r') as f:
        redirects = json.load(f)

    # Load the HTML template
    with open('redirect-template.html', 'r') as f:
        template = f.read()

    # Create directories and index files for each slug
    for slug, url in redirects.items():
        os.makedirs(slug, exist_ok=True)
        with open(f"{slug}/index.html", "w", encoding="utf-8") as f:
            # Inject the target URL into the template
            f.write(template.replace("{{URL}}", url))
        print(f"✅ Generated: /{slug} -> {url}")

if __name__ == "__main__":
    generate_redirects()
