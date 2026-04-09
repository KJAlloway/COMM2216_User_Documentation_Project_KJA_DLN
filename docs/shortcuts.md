# Keyboard Shortcuts

## Overview

IntelliJ IDEA has keyboard shortcuts for nearly every action in the IDE.
Learning even a small set of core shortcuts will meaningfully reduce the
time you spend navigating menus and let you stay focused on your code.

This section explains how [keymaps](glossary.md#keymap) work in IntelliJ IDEA,
walks through the shortcuts most relevant to CST coursework, and shows you
how to find and customize shortcuts to match your own preferences.

By the end of this section you will know the most useful shortcuts for
daily coursework and how to reassign any shortcut that does not work
well for you.

## Understanding Keymaps

A [keymap](glossary.md#keymap) is a complete mapping of keyboard shortcuts
to IDE actions. IntelliJ IDEA stores your active keymap as a file that can
be shared and imported. When you modify a predefined keymap, IDEA automatically
creates a copy — the original is never changed.

To view your current keymap:

1. Open **File > Settings** (++ctrl+alt+s++).
2. Select **Keymap** from the left panel.

    At this point, you will see your active keymap in the dropdown at
    the top of the panel and a full searchable list of actions below.

## Shortcuts Reference

### Line Editing

| Shortcut | Action | Notes |
|---|---|---|
| ++ctrl+y++ | Delete current line | Removes the entire line under the [caret](glossary.md#caret) |
| ++ctrl+d++ | Duplicate line or selection | Duplicates current line, or duplicates and appends a selection |
| ++shift+enter++ | Start new line below | Moves to a new line without breaking the current one, regardless of [caret](glossary.md#caret) position |
| ++ctrl+shift+j++ | Join lines | Merges the next line up into the current line |
| ++alt+shift+up++ | Move line up | Shifts the current line up one position |
| ++alt+shift+down++ | Move line down | Shifts the current line down one position |
| ++ctrl+shift+up++ | Move statement up | Moves an entire code block — method, if block, loop — up |
| ++ctrl+shift+down++ | Move statement down | Moves an entire code block down |

!!! tip
    There is an important difference between Move Line and Move Statement.
    Move Line (++alt+shift+up++ / ++alt+shift+down++) moves only the single
    line your [caret](glossary.md#caret) is on. Move Statement
    (++ctrl+shift+up++ / ++ctrl+shift+down++) moves the entire logical
    block — so if your caret is inside a method body, the whole method
    moves. Use Move Statement when reorganising methods; use Move Line
    for adjustments within a block.

### Navigation

| Shortcut | Action | Notes |
|---|---|---|
| ++end++ or ++fn+arrow-right++ | Go to end of line | `End` on full keyboards; `Fn+Right` on laptops |
| ++home++ or ++fn+arrow-left++ | Go to start of line | `Home` on full keyboards; `Fn+Left` on laptops |
| ++ctrl+b++ | Go to declaration | Jumps to where a method, class, or variable is defined |
| ++ctrl+e++ | Recent files | Quickly switch between recently opened files |
| ++alt+1++ | Show Project [tool window](glossary.md#tool-window) | Toggles the file tree panel open and closed |
| ++escape++ | Return focus to editor | Works from any tool window or search dialog |
| ++shift+shift++ | Search Everywhere | Find any file, class, action, or setting — press Shift twice |
| ++ctrl+shift+a++ | Find Action | Search for any IDE action by name — useful when you forget a shortcut |

### Multiple Carets

Multiple [carets](glossary.md#caret) let you edit several locations in a file
simultaneously. This is useful for renaming a variable in multiple places
without using a full rename [refactor](glossary.md#refactoring), or for adding
the same text to several lines at once.

IntelliJ IDEA provides two complementary ways to place multiple carets:

**By clicking specific locations:**

| Shortcut | Action |
|---|---|
| ++alt+shift+click++ | Add or remove a caret at the clicked location |
| ++ctrl+click++ | Add a caret at the clicked location (alternative) |

**By keyboard on adjacent lines:**

| Shortcut | Action |
|---|---|
| ++ctrl++ twice, then ++up++ | Clone caret on the line above |
| ++ctrl++ twice, then ++down++ | Clone caret on the line below |
| ++alt+j++ | Select next occurrence of word under caret |
| ++ctrl+alt+shift+j++ | Select all occurrences of word under caret in file |

Press ++escape++ to return to a single caret.

!!! tip
    Multiple carets are especially useful when adding `final` to method
    parameters. Place a caret before each parameter type using
    ++alt+shift+click++, then type `final ` once to insert it at all
    caret positions simultaneously.

### Code Generation and Formatting

| Shortcut | Action | Notes |
|---|---|---|
| ++ctrl+s++ | Save all | Also triggers Save Actions X if configured |
| ++ctrl+alt+l++ | Reformat code | Applies your [code style](glossary.md#code-style) settings to the file |
| ++alt+insert++ | Open Generate menu | Generate getters, setters, constructors, `toString`, `equals`, `hashCode` |
| ++alt+enter++ | Show context actions | Quick-fixes for inspection warnings and errors |
| ++ctrl+slash++ | Toggle line comment | |
| ++ctrl+shift+slash++ | Toggle block comment | |

#### Assigning a Javadoc Shortcut

There is no default shortcut for Generate Javadoc. If you want one,
see [Customizing Your Keymap](#customizing-your-keymap) below for
instructions on assigning your own shortcut.

### Code Analysis

| Shortcut | Action | Notes |
|---|---|---|
| ++f2++ | Jump to next error or warning | Cycles through inspection findings in the current file |
| ++shift+f2++ | Jump to previous error or warning | |
| ++ctrl+alt+shift+i++ | Run inspection by name | Run a specific [inspection](glossary.md#code-inspection) on demand |
| ++alt+enter++ | Show context actions | See suggested fixes for the highlighted issue |

### Refactoring

| Shortcut | Action | Notes |
|---|---|---|
| ++ctrl+alt+shift+t++ | Open Refactor menu | Access all [refactoring](glossary.md#refactoring) options |
| ++shift+f6++ | Rename | Renames a variable, method, or class and updates every reference |
| ++ctrl+alt+m++ | Extract method | Extracts selected code into a new method |
| ++ctrl+alt+v++ | Introduce variable | Extracts an expression into a named local variable |

## Customizing Your Keymap

IntelliJ IDEA makes it straightforward to find and reassign any shortcut.
You can search by action name or by the key combination itself.

### Finding a Shortcut by Action Name

1. Open **File > Settings** (++ctrl+alt+s++).

2. Navigate to **Keymap**.

3. **Type** the name of the action in the search field at the top of
   the Keymap panel — for example, `Generate JavaDocs for selected element`.

    At this point, the list filters to show only matching actions, with
    their current shortcut assignments shown beside them.

### Finding Which Action a Key Combination Is Assigned To

1. Open **File > Settings** (++ctrl+alt+s++).

2. Navigate to **Keymap**.

3. Click the **Find Action by Shortcut** button — the magnifying glass
   icon to the right of the search field.

4. Press the key combination you want to look up.

    At this point, the panel shows every action currently assigned to
    that combination.

### Assigning or Reassigning a Shortcut

1. Find the action you want to reassign using either method above.

2. **Right-click** the action and select **Add Keyboard Shortcut**.

3. Press your desired key combination in the dialog that appears.

    At this point, IntelliJ IDEA will warn you if the combination is
    already in use by another action. Review the conflict and decide
    whether to reassign or choose a different combination.

4. Click **OK** to save.

!!! note
    When you modify any shortcut, IntelliJ IDEA creates a copy of the
    predefined keymap rather than editing it directly. Your customized
    keymap will appear in the dropdown with a name like
    **Windows copy**. The original keymap is preserved and you can
    revert to it at any time by selecting it from the dropdown.

## Learning Shortcuts as You Work

The Key Promoter X plugin installed in
[Installing and Configuring Plugins](plugins.md) will display a popup
whenever you use the mouse for an action that has a keyboard shortcut.
This is the most practical way to build shortcut habits without stopping
to memorise a list.

You can also access a printable shortcut reference card at any time via
**Help > Keyboard Shortcuts PDF**.

## Conclusion

Your IntelliJ IDEA environment is now fully configured for CST coursework:

- IntelliJ IDEA Ultimate is installed and licenced
- AI completion is disabled to comply with course requirements
- Your settings sync across devices via your JetBrains account
- Your inspection profile provides live feedback aligned with course
  style requirements
- Recommended plugins are installed, including CheckStyle-IDEA for
  pre-submission verification
- You know the core shortcuts and how to customize any that do not
  work for you

If you run into problems at any point, see the
[Troubleshooting Guide](troubleshooting.md).
