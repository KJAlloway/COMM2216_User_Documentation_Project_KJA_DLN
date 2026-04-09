# IntelliJ IDEA User Guide for CST Students

A user documentation site built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/),
written for students entering the Computer Systems Technology (CST) program at BCIT in September 2026.

## About This Guide

This guide covers four core tasks for setting up and customising IntelliJ IDEA
as your primary IDE for CST coursework:

1. **Installation and Student Account Setup** — Downloading IDEA, activating a
   JetBrains Education licence, and syncing settings across devices
2. **Configuring Inspections** — Understanding code inspections, adjusting them
   to match class style guides, and applying provided inspection profiles
3. **Installing and Configuring Plugins** — Recommended plugins for CST students
   and how to set them up
4. **Keyboard Shortcuts** — Most useful shortcuts, recommendations, and applying
   a pre-configured keymap

## Repository Structure

```
docs/                        # MkDocs source files (Markdown)
resources/
  inspection-profiles/       # CST_Inspections.xml and COMP-2522-Checkstyle.xml
  keymaps/                   # CST_Keymap.xml
.github/workflows/           # GitHub Actions deployment workflow
mkdocs.yml                   # MkDocs site configuration
requirements.txt             # Python dependencies
```

## Getting Started (For Contributors)

### Prerequisites

- Python 3.x installed and on your PATH
- Git

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/KJAlloway/COMM2216_User_Documentation_Project_KJA_DLN.git
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start the local development server:
   ```
   mkdocs serve
   ```

5. Open `http://localhost:8000` in your browser. The site live-reloads as
   you edit.

!!! note
    The `venv/` folder is excluded from version control. You must recreate
    it locally after every fresh clone using the steps above.

## Deployment

This repository uses a GitHub Actions workflow (`.github/workflows/deploy.yml`)
that automatically builds and deploys the site to GitHub Pages on every push
to the `main` branch. No manual deploy steps are required.

The live site is available at:
[https://kjalloway.github.io/COMM2216_User_Documentation_Project_KJA_DLN/](https://kjalloway.github.io/COMM2216_User_Documentation_Project_KJA_DLN/)

## Process and Methods

This documentation was developed following the instruction writing principles
from BCIT's COMM 2216 course, applied to a real-world software configuration
context.

The process began with task analysis — identifying the four setup tasks a new
CST student would need to complete before their first day of class, and
sequencing them so each task builds on the previous one. We used walkthroughs
of each task in the actual IDE to identify every required step, determine where
screenshots and GIFs would aid comprehension, and anticipate where students
were likely to encounter errors.

Content was drafted iteratively, with each section reviewed against the COMP
2522 Style Guide and Checkstyle configuration to ensure the inspection and
plugin guidance reflected real course requirements rather than generic advice.
The troubleshooting guide was populated from problems encountered during our
own setup process.

The site is built with MkDocs Material and hosted via GitHub Pages, with
automatic deployment on every push. Configuration files — the inspection
profile XML, Checkstyle XML, and keymap XML — were authored to match course
requirements and are distributed alongside the documentation so students can
import them directly rather than configuring the IDE manually.

Peer testing was conducted in labs with classmates following the instructions
cold, and feedback from that session was incorporated before final submission.

## Built With

- [MkDocs](https://www.mkdocs.org/)
- [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
- GitHub Actions for automated deployment
- GitHub Pages for hosting

## Authors

- Kelsen Alloway — [@KJAlloway](https://github.com/KJAlloway)
- Donovan — [@donovanthereal](https://github.com/donovanthereal)
