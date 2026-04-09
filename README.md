# IntelliJ IDEA User Guide for CST Students

A user documentation site built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), written for
students entering the Computer Systems Technology (CST) program at BCIT in September 2026.

## About This Guide

This guide covers four core tasks for setting up and customising IntelliJ IDEA as your primary IDE for CST coursework:

1. **Installation & Student Account Setup** — Downloading IDEA, activating a JetBrains Education licence, and syncing
   settings across devices
2. **Configuring Inspections** — Understanding code inspections, adjusting them to match class style guides, and
   applying provided inspection profiles
3. **Installing & Configuring Plugins** — Recommended plugins for CST coursework and how to set them up
4. **Keyboard Shortcuts** — Most useful shortcuts, recommendations, and applying a pre-configured keymap

## Repository Structure

```
docs/                  # MkDocs source files (Markdown)
resources/             # Downloadable config files
  inspection-profiles/ # Custom inspection XML profiles for CST courses
  keymaps/             # Pre-configured keymap files
mkdocs.yml             # MkDocs site configuration
requirements.txt       # Python dependencies
```

## Getting Started (For Contributors)

### Prerequisites

- Python 3.x installed and on your PATH
- Git

### Setup

1. Clone the repository:

```
   git clone <repo-url>
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
   mkdocs serve --livereload
```

5. Open `http://localhost:8000` in your browser. The site will live-reload as you edit.

> **Note:** The `venv/` folder is excluded from version control. You must recreate it locally after every fresh clone
> using the steps above.

## Built With

- [MkDocs](https://www.mkdocs.org/)
- [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)

## Authors

- Kelsen [KJALLOWAY]
- Donovan [donovanthereal]