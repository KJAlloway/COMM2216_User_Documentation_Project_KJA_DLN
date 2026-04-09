# IntelliJ IDEA Setup Guide for CST Students

[IntelliJ IDEA](https://www.jetbrains.com/idea/) is a professional integrated
development environment (IDE) built by JetBrains. It provides intelligent code
completion, built-in debugging tools, version control integration, and a
plugin ecosystem that extends its functionality for different languages and
frameworks. Throughout the CST program, you will use IntelliJ IDEA as your
primary environment for writing, testing, and debugging Java and Kotlin code.

This guide walks you through the initial setup and configuration of IntelliJ IDEA
so that your environment is ready before your first day of classes.

## Is This Guide for You?

This guide is written for students entering BCIT's Computer Systems Technology
program in September 2026 who have not previously used IntelliJ IDEA or any
other JetBrains IDE. No prior configuration experience is required.

To follow this guide you will need:

- A computer running Windows 10 or later, macOS 12 or later, or a
  supported Linux distribution
- A BCIT student email address (format: `firstname_lastname@my.bcit.ca`)
- An active internet connection
- [Java Development Kit (JDK) 21](https://www.oracle.com/java/technologies/downloads/#java21)
  installed on your computer

## By the End of This Guide You Will Be Able To

1. Install IntelliJ IDEA and activate a free JetBrains Education licence
   using your BCIT student email
2. Sync your IDE settings across multiple devices using a JetBrains account
3. Configure code inspections to match the style requirements used in
   CST courses
4. Install and configure plugins recommended for CST coursework
5. Apply a pre-configured keymap and learn the shortcuts most relevant
   to your daily workflow

## What This Guide Covers

The tasks in this guide are designed to be completed in order. Each task builds
on the previous one, and the final task — keyboard shortcuts — is intentionally
last so your keymap reflects all other configuration choices.

1. [Installation and Student Account Setup](installation.md) — Install
   IntelliJ IDEA, activate your free Education licence, and configure
   settings sync across devices
2. [Configuring Inspections](inspections.md) — Understand what code
   inspections do, and apply inspection profiles configured for CST
   course style requirements
3. [Installing and Configuring Plugins](plugins.md) — Install plugins
   recommended for CST students and configure them for coursework
4. [Keyboard Shortcuts](shortcuts.md) — Apply a pre-configured keymap
   and learn the shortcuts most relevant to your daily workflow

## Downloadable Configuration Files

This guide includes ready-to-use configuration files hosted in the
[`/resources`](https://github.com/KJAlloway/COMM2216_User_Documentation_Project_KJA_DLN/tree/main/resources)
folder of this repository:

- **Inspection profile** — `CST_Inspections.xml`, pre-configured to match
  COMP 2522 style requirements, referenced in
  [Configuring Inspections](inspections.md)
- **Checkstyle configuration** — `COMP-2522-Checkstyle.xml`, the course
  Checkstyle ruleset your instructor grades against, referenced in
  [Installing and Configuring Plugins](plugins.md)
- **Keymap** — `CST_Keymap.xml`, a pre-configured keymap with one addition
  to the IntelliJ IDEA defaults, referenced in
  [Keyboard Shortcuts](shortcuts.md)

## Typographical Conventions

This guide uses the following conventions throughout:

| Convention | Use | Example |
|---|---|---|
| **Bold** | UI elements: buttons, menus, tabs, and labels | Click **OK** |
| `Monospace` | File names, paths, and code | `CST_Inspections.xml` |
| **Menu > Item** | A sequence of menu selections | **File > Settings > Keymap** |
| *Italics* | A new term being introduced for the first time | The *Project* tool window |
| Key badges | A physical key or key combination to press | ++ctrl+alt+s++ |

Keyboard shortcuts in this guide use the default Windows keymap. Where macOS
shortcuts differ significantly, they are noted in parentheses.

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
