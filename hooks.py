"""
MkDocs hooks:

1. linked_abbr: Wraps <abbr> tags with glossary links, giving every glossary
   term a hover tooltip AND a clickable link to the full definition.
   Skips abbr tags that are already inside an <a> tag (e.g. the JDK Oracle
   download link) to avoid invalid nested <a><a> HTML.
   Skips the glossary page itself.

2. external_links: Adds target="_blank" to all external links.

Place this file at docs/hooks.py and add to mkdocs.yml:
    hooks:
      - docs/hooks.py
"""

import re

ABBR_TO_ANCHOR = {
    "integrated development environment": "ide",
    "IDE": "ide",
    "JDK": "jdk",
    "JVM": "jdk",
    "Kotlin": "kotlin",
    "Checkstyle": "checkstyle",
    "Checkstyle configuration": "checkstyle-configuration",
    "Javadoc": "javadoc",
    "JetBrains account": "jetbrains-account",
    "Settings sync": "settings-sync",
    "settings sync": "settings-sync",
    "Keymap": "keymap",
    "keymap": "keymap",
    "keymaps": "keymap",
    "Plugins": "plugin",
    "plugin": "plugin",
    "plugins": "plugin",
    "tool window": "tool-window",
    "tool windows": "tool-window",
    "Code inspections": "code-inspection",
    "code inspections": "code-inspection",
    "code inspection": "code-inspection",
    "inspection": "code-inspection",
    "inspections": "code-inspection",
    "inspection profile": "profile",
    "Inspection profile": "profile",
    "severity": "severity",
    "static analysis": "static-analysis",
    "code style": "code-style",
    "caret": "caret",
    "carets": "caret",
    "indexing": "indexing",
    "String": "string",
    "string": "string",
    "strings": "string",
    "stub": "stub",
    "stubs": "stub",
    "Wildcard imports": "wildcard-import",
    "Magic number": "magic-number",
    "Magic numbers": "magic-number",
    "refactoring": "refactoring",
    "refactor": "refactoring",
    "scope": "scope-ide-settings",
    "superclass": "superclass",
    "Annotation": "annotation",
    "Build tool": "build-tool",
    "Profile": "profile",
    "Run configuration": "run-configuration",
    "UML": "uml",
    "Velocity template": "velocity-template",
    "Lint": "lint",
    "linting": "lint",
}

GLOSSARY_SRC = "glossary.md"


def on_page_content(html, page, config, **kwargs):
    html = _link_abbr_to_glossary(html, page)
    html = _external_links_new_tab(html)
    return html


def _glossary_base(page):
    """
    Return the correct relative URL prefix to reach the glossary page.
    With use_directory_urls (MkDocs default):
      index.md  -> served at /          -> glossary at glossary/
      other.md  -> served at /other/    -> glossary at ../glossary/
    """
    if page.file.src_path == "index.md":
        return "glossary/"
    return "../glossary/"


def _link_abbr_to_glossary(html, page):
    """
    Wrap <abbr> tags with a glossary <a> link.
    Skips the glossary page itself.

    <abbr> tags that already sit inside an existing <a> tag are stripped
    down to plain text — they are already part of a link (page or external)
    and should not show a dotted underline or nested glossary link.
    """
    if page.file.src_path == GLOSSARY_SRC:
        return html

    base = _glossary_base(page)

    # Step 1: inside any existing <a>...</a>, unwrap <abbr> to plain text.
    def strip_abbr_inside_a(a_match):
        return re.sub(r'<abbr [^>]+>([^<]+)</abbr>', r'\1', a_match.group(0))

    html = re.sub(r'<a\b[^>]*>.*?</a>', strip_abbr_inside_a, html, flags=re.DOTALL)

    # Step 2: wrap remaining bare <abbr> tags (outside any <a>) with glossary links.
    def replace_abbr(match):
        attrs  = match.group(1)
        term   = match.group(2)
        anchor = ABBR_TO_ANCHOR.get(term)
        if not anchor:
            return match.group(0)

        url = f"{base}#{anchor}"
        return (
            f'<a href="{url}" class="glossary-link">'
            f'<abbr {attrs}>{term}</abbr>'
            f'</a>'
        )

    return re.sub(r'<abbr ([^>]+)>([^<]+)</abbr>', replace_abbr, html)


def _external_links_new_tab(html):
    """Add target="_blank" to all external links that don't already have it."""
    return re.sub(
        r'<a (href="https?://[^"]+")(?![^>]*target=)([^>]*)>',
        r'<a \1 target="_blank" rel="noopener noreferrer"\2>',
        html,
    )
