# IntelliJ IDEA Setup Guide for CST Students

[IntelliJ IDEA](https://www.jetbrains.com/idea/) is a professional
integrated development environment (IDE) built by JetBrains.
It provides intelligent code completion, built-in debugging tools, version
control integration, and a plugin ecosystem that extends its functionality
for different languages and frameworks. Throughout the CST program, you will
use IntelliJ IDEA as your primary environment for writing, testing, and
debugging Java and Kotlin code.

This guide walks you through the initial setup and configuration of IntelliJ IDEA
so that your environment is ready before your first day of classes.

## Is This Guide for You?

This guide is written for students entering BCIT's Computer Systems Technology
program who have not previously used IntelliJ IDEA or any other JetBrains IDE.
No prior configuration experience is required.

To follow this guide you will need:

- A computer running Windows 10 or later, macOS 12 or later, or a
  supported Linux distribution
- A BCIT student email address (format: `firstname_lastname@my.bcit.ca`)
- An active internet connection
- [Java Development Kit (JDK) 25](https://www.oracle.com/java/technologies/downloads/#java25)
  installed on your computer

## By the End of This Guide You Will Be Able To

1. Install IntelliJ IDEA and activate a free JetBrains Education licence
   using your BCIT student email
2. Sync your IDE settings across multiple devices using a JetBrains account
3. Configure code inspections to match the style requirements used in CST courses
4. Install and configure plugins recommended for CST coursework
5. Apply a keymap and learn the shortcuts most relevant to your daily workflow
6. Configure code generation templates for COMP 2522-compliant
   `equals()`, `hashCode()`, and `toString()` methods

## What This Guide Covers

The tasks in this guide are designed to be completed in order. Each task builds
on the previous one, and the final task — code templates — is intentionally
last because it builds on the inspection profile and plugin configuration from
earlier sections.

1. [Installation and Student Account Setup](installation.md) — Install
   IntelliJ IDEA, activate your free Education licence, and configure
   settings sync across devices
2. [Installing and Configuring Plugins](plugins.md) — Install plugins
   recommended for CST students, disable AI completion tools, and
   configure them for coursework
3. [Configuring Inspections](inspections.md) — Understand what code
   inspections do, and apply inspection profiles configured for CST
   course style requirements
4. [Keyboard Shortcuts](shortcuts.md) — Learn the shortcuts most relevant
   to your daily workflow and customize your keymap
5. [Configuring Code Templates](templates.md) — Set up `equals()`,
   `hashCode()`, `toString()`, and Javadoc templates to generate
   COMP 2522-compliant code automatically

## Downloadable Configuration Files

This guide includes ready-to-use configuration files hosted in the
[`/resources`](https://github.com/KJAlloway/COMM2216_User_Documentation_Project_KJA_DLN/tree/main/resources)
folder of this repository:

- **Inspection profile** — `CST_Inspections.xml`, pre-configured to match
  COMP 2522 requirements, referenced in [Configuring Inspections](inspections.md)
- **Checkstyle configuration** — `COMP-2522-Checkstyle.xml`, the course
  Checkstyle ruleset your instructor grades against,
  referenced in [Installing and Configuring Plugins](plugins.md)

## Conventions

This guide uses the following typographical and link conventions:

| Convention | Use | Example |
|---|---|---|
| **Bold** · **Bold > Bold** | UI elements, buttons, labels, and menu selection sequences | Click **OK** · **File > Settings > Keymap** |
| `Monospace` | File names, paths, code, or exact input values | `CST_Inspections.xml` |
| *Italics* | A new term being introduced for the first time | The *Project* tool window |
| Key badges | A key or key combination to press | ++ctrl+alt+s++ |
| [External link](https://www.jetbrains.com/idea/) | A link to a website outside this guide — opens in a new tab | [JetBrains website](https://www.jetbrains.com/idea/) |
| [Internal link](installation.md) | A link to another page within this guide | [Installation and Student Account Setup](installation.md) |
| Glossary term | A dotted underline indicates a defined term — hover for a quick definition, click to see the full Glossary entry | integrated development environment (IDE) |

Keyboard shortcuts in this guide cover both operating systems. Use the
**Windows / macOS** toggle button in the top-right of the header to switch
all shortcut tables at once. Your choice is saved and applied automatically
on every page.

## Admonitions

This guide uses four types of notices. Each appears before the step or
section it applies to:

!!! note
    Provides helpful context or extra information. Skipping a note will
    not cause errors, but reading it will improve your understanding.

!!! tip
    Highlights a faster or recommended approach that saves time or effort.

!!! warning
    Flags something that may produce unexpected results if ignored.
    Read before performing the associated step.

!!! danger
    Identifies an action that could cause data loss or require
    reinstallation to recover from. Do not proceed without reading.
