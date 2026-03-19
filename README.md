# 🔗 rect

**rect | to redirect wherever.** is a minimalist, open-source URL shortener that runs entirely on GitHub Pages. No servers, no databases, just pure static speed.

## ⚡ Features
- **Instant Redirects:** No 404-latency. Uses pre-generated folders.
- **Serverless:** Hosted for free on GitHub Pages.
- **Automated:** Managed via GitHub Actions and a simple `redirects.json`.
- **Modern UI:** Clean, dark-mode landing and error pages.

## 🚀 Quick Start
1. **Fork this repo.**
2. **Edit `redirects.json`** to add your links:
   ```json
   { "my-link": "[https://example.com](https://example.com)" }
