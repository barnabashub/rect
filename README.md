# 🔗 rect

**rect | redirect wherever.** is a high-performance, minimalist, and 100% static URL shortener designed to run entirely on **GitHub Pages**. No servers, no databases, no costs—just pure speed and automation.

---

- **Zero Latency:** Direct folder-based routing.
- **Serverless:** Hosted for free on GitHub.
- **Automated:** Updates itself via GitHub Actions whenever you edit your links.

---

## 🚀 Getting Started

### 1. Setup the Repository
1. **Fork** this repository or create a new one using these files.
2. Ensure you have a `redirects.json` file in the root directory.

### 2. Configure Your Links
Edit `redirects.json` to include your desired slugs and destination URLs:
```json
{
  "gh": "[https://github.com/yourusername/rect](https://github.com/yourusername/rect)",
  "blog": "[https://yourwebsite.com/posts/my-awesome-article](https://yourwebsite.com/posts/my-awesome-article)",
  "social": "[https://twitter.com/yourhandle](https://twitter.com/yourhandle)"
}
```
### 3. Deployment
Push your changes to the main branch.

The GitHub Action will automatically trigger, run the Python generator, and push the results to a gh-pages branch.

Go to Settings > Pages in your GitHub repo:

Under Build and deployment, set the source to Deploy from a branch.

Select the gh-pages branch and / (root) folder.

Click Save.

Your links will now be live at https://yourusername.github.io/rect.

---

🛠 Tech Stack
Logic: Python 3 (Static Generator)

Automation: GitHub Actions

Hosting: GitHub Pages

Styling: Modern CSS3 with Glassmorphism effects

📁 File Structure
redirects.json: Your link database.

generator.py: The engine that builds the directory structure.

redirect-template.html: The HTML snippet used for each redirect.

index.html: The public-facing landing page.

404.html: The custom error page for broken links.

.github/workflows/deploy.yml: The automation script.

---

🤝 Contributing
Contributions are welcome! Whether it's a new feature, a bug fix, or a UI improvement, feel free to open a Pull Request.


⚖️ License
Distributed under the MIT License. See LICENSE for more information.
