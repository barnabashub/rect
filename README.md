# 🔗 rect

**rect | redirect wherever.** is a high-performance, minimalist, and 100% static URL shortener designed to run entirely on **GitHub Pages**. No servers, no databases, no costs—just pure speed and automation.

---

- **Zero Latency:** Direct folder-based routing.
- **Serverless:** Hosted for free on GitHub.
- **Automated:** Updates itself via GitHub Actions whenever you edit your links.

---

## How It Works

1. **Source:** You manage `redirects.json` and your UI templates in the root.
2. **Build:** The Python script (`generator.py`) wipes the `public/` folder and regenerates everything:
   - Copies `index.html` and `404.html`.
   - Creates a folder for each **slug** (e.g., `/fb`, `/twitter`).
   - Places a redirecting `index.html` inside each slug folder.
3. **Deploy:** GitHub Actions deploys **only** the contents of the `public/` folder to the web.

---

## 🚀 Getting Started

1. Setup the Repository
Fork this repository or create a new one using these files.

Enable Write Permissions (Crucial for the automation):

Go to Settings > Actions > General.

Scroll to Workflow permissions.

Select Read and write permissions and click Save.

2. Configure Your Links
Edit redirects.json in the root directory to include your desired slugs and destination URLs:

JSON
{
  "gh": "https://github.com/yourusername/slynk",
  "demo": "https://example.com/live-demo"
}

3. Automatic Build
Push your changes to the main branch.

Click the Actions tab at the top to watch the "Build & Deploy" workflow.

Once it finishes (green checkmark), a new branch called gh-pages will be created automatically.

4. Enable GitHub Pages
Go to Settings > Pages.

Under Build and deployment > Branch:

Select gh-pages.

Ensure the folder is set to /(root).

Click Save.

Your links will be live at https://yourusername.github.io/slug within a minute!
---

🛠 Tech Stack
Logic: Python 3 (Static Generator)

Automation: GitHub Actions

Hosting: GitHub Pages

Styling: Modern CSS3 with Glassmorphism effects

📁 Project Structure

- redirects.json: Your link database.
- generator.py: The engine that builds the directory structure.
- public/ — (Generated) This is what actually goes live.
- .github/workflows/deploy.yml: The automation script.

---

🤝 Contributing
Contributions are welcome! Whether it's a new feature, a bug fix, or a UI improvement, feel free to open a Pull Request.


⚖️ License
Distributed under the MIT License. See LICENSE for more information.
