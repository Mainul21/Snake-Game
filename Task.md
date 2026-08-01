# AI Agent Task: Prepare Snake Game for Web Deployment

## Objective

Prepare this Python Snake Game repository for deployment as a browser-playable game using **Pygbag** and GitHub Pages.

The goal is to produce a clean, professional repository suitable for a portfolio and CV.

---

# Tasks

## 1. Analyze the Project

* Determine which Python game library/framework is being used.
* Identify the application's entry point.
* Detect all required assets (images, fonts, sounds, etc.).
* Ensure all asset paths are relative.

---

## 2. Remove Unnecessary Files

Delete files and folders that are not required for running or publishing the game, including but not limited to:

* `__pycache__/`
* `.pytest_cache/`
* `.mypy_cache/`
* `.idea/`
* `.vscode/` (except recommended settings if useful)
* Temporary build folders
* Old executables
* `.DS_Store`
* `Thumbs.db`
* Log files
* Backup files
* Unused screenshots
* Unused assets
* Duplicate files

Do **not** remove any files required by the game.

---

## 3. Improve Project Structure

Organize the project into a clean layout if needed:

```text
Snake-Game/
│
├── assets/
│   ├── images/
│   ├── sounds/
│   └── fonts/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── ...
```

Only reorganize files if it does not break imports.

---

## 4. Code Cleanup

Without changing gameplay:

* Remove dead code.
* Remove unused imports.
* Remove unused variables.
* Remove duplicate logic.
* Improve readability.
* Follow PEP 8 where practical.
* Keep the code beginner-friendly.

Do **not** rewrite the project into a different architecture.

---

## 5. Prepare for Pygbag

Modify the project if necessary so it can run with:

```bash
python -m pygbag .
```

Ensure:

* Relative file paths only.
* No absolute paths.
* No Windows-only functionality.
* Assets load correctly.
* Fonts load correctly.
* Audio works if possible.
* The game exits gracefully in a browser.

---

## 6. Dependency Management

Create or update `requirements.txt` containing only the required packages.

Remove unnecessary dependencies.

---

## 7. Create `.gitignore`

Include common Python exclusions such as:

* `__pycache__/`
* `*.pyc`
* `.venv/`
* `venv/`
* `.idea/`
* `.vscode/`
* Build artifacts
* OS-generated files

---

## 8. Improve README

Create a professional README that includes:

* Project title
* Screenshot placeholder
* Features
* Controls
* Installation
* Local execution
* Web deployment (Pygbag)
* Technologies used
* Repository structure
* Future improvements
* License

Include sections for:

```markdown
## Live Demo

(Add GitHub Pages link here)

## GitHub Repository

(Add repository URL here)
```

---

## 9. Browser Compatibility

Check for features unsupported by browsers.

If changes are required for Pygbag compatibility:

* Explain why.
* Apply the smallest possible fix.
* Preserve existing gameplay.

---

## 10. Final Verification

Verify that:

* The game runs locally.
* The game builds with Pygbag.
* No missing assets exist.
* No broken imports remain.
* No unused files remain.
* The repository is clean and ready for GitHub.

---

# Deliverables

Provide:

1. A summary of all changes made.
2. A list of deleted files.
3. A list of modified files.
4. Any compatibility issues found.
5. Any manual steps still required.
6. Confirmation that the project is ready for GitHub Pages deployment using Pygbag.

Do not make unnecessary architectural changes. Preserve the existing gameplay and behavior unless a change is required for browser compatibility.
