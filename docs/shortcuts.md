# Keyboard Shortcuts

## Overview

IntelliJ IDEA has keyboard shortcuts for nearly every action in the IDE.
Learning even a small set of core shortcuts will meaningfully reduce the
time you spend navigating menus and let you stay focused on your code.

This section explains how keymaps work in IntelliJ IDEA, walks through
the shortcuts most relevant to CST coursework, and guides you through
applying the pre-configured CST keymap provided with this guide.

By the end of this section your IDE will have the CST keymap active.

!!! note
    The CST keymap is based on the default Windows keymap with one
    targeted addition: ++ctrl+l++ as a second shortcut for Reformat Code.
    All other shortcuts listed in this section are unchanged from the
    IntelliJ IDEA defaults. The goal is a clean, conflict-free setup
    you can rely on throughout your time in CST.

## Understanding Keymaps

A *keymap* is a complete mapping of keyboard shortcuts to IDE actions.
IntelliJ IDEA stores your active keymap as a file that can be shared
and imported. When you modify a predefined keymap, IDEA automatically
creates a copy — the original is never changed.

To view your current keymap:

1. Open **File > Settings** (++ctrl+alt+s++).
2. Select **Keymap** from the left panel.

    At this point, you will see your active keymap in the dropdown at
    the top of the panel and a full searchable list of actions below.

## CST Keymap Change from Default

The CST keymap makes one change from the IntelliJ IDEA defaults:

| Action | Default | CST Keymap |
|---|---|---|
| Reformat Code | ++ctrl+alt+l++ | ++ctrl+l++ *(added as additional shortcut)* |

++ctrl+l++ is added as a second shortcut for Reformat Code alongside
the existing ++ctrl+alt+l++. Both work — ++ctrl+l++ is simply faster
to press during active editing. No default shortcut is removed.

!!! note
    On some Windows systems, ++ctrl+alt+l++ conflicts with the system
    screen lock shortcut. If Reformat Code does not work on your machine,
    ++ctrl+l++ from the CST keymap will work regardless.

## Shortcuts Reference

### Line Editing

| Shortcut | Action | Notes |
|---|---|---|
| ++ctrl+y++ | Delete current line | Removes the entire line under the caret |
| ++ctrl+d++ | Duplicate line or selection | Duplicates current line, or duplicates and appends a selection |
| ++shift+enter++ | Start new line below | Moves to a new line without breaking the current one, regardless of caret position |
| ++ctrl+shift+j++ | Join lines | Merges the next line up into the current line |
| ++alt+shift+up++ | Move line up | Shifts the current line up one position |
| ++alt+shift+down++ | Move line down | Shifts the current line down one position |
| ++ctrl+shift+up++ | Move statement up | Moves an entire code block — method, if block, loop — up |
| ++ctrl+shift+down++ | Move statement down | Moves an entire code block down |

!!! tip
    There is an important difference between Move Line and Move Statement.
    Move Line (++alt+shift+up/down++) moves only the single line your
    caret is on. Move Statement (++ctrl+shift+up/down++) moves the entire
    logical block — so if your caret is inside a method body, the whole
    method moves. Use Move Statement when reorganising methods; use Move
    Line for adjustments within a block.

### Navigation

| Shortcut | Action | Notes |
|---|---|---|
| ++end++ or ++fn+arrow-right++ | Go to end of line | `End` on full keyboards; `Fn+Right` on laptops |
| ++home++ or ++fn+arrow-left++ | Go to start of line | `Home` on full keyboards; `Fn+Left` on laptops |
| ++ctrl+b++ | Go to declaration | Jumps to where a method, class, or variable is defined |
| ++ctrl+e++ | Recent files | Quickly switch between recently opened files |
| ++alt+1++ | Show Project tool window | Toggles the file tree panel open and closed |
| ++escape++ | Return focus to editor | Works from any tool window or search dialog |
| ++double-shift++ | Search Everywhere | Find any file, class, action, or setting |
| ++ctrl+shift+a++ | Find Action | Search for any IDE action by name — useful when you forget a shortcut |

### Multiple Carets

Multiple carets let you edit several locations in a file simultaneously.
This is useful for renaming a variable in multiple places without using
a full rename refactor, or for adding the same text to several lines
at once.

IntelliJ IDEA provides two complementary ways to place multiple carets:

**By clicking specific locations:**

| Shortcut | Action |
|---|---|
| ++alt+shift+click++ | Add or remove a caret at the clicked location |
| ++ctrl+click++ | Add a caret at the clicked location (alternative) |

**By keyboard on adjacent lines:**

| Shortcut | Action |
|---|---|
| Double ++ctrl++ + ++up++ | Clone caret on the line above |
| Double ++ctrl++ + ++down++ | Clone caret on the line below |
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
| ++ctrl+l++ | Reformat code | CST keymap addition — also available as ++ctrl+alt+l++ |
| ++alt+insert++ | Open Generate menu | Generate getters, setters, constructors, `toString`, `equals`, `hashCode` |
| ++alt+enter++ | Show context actions | Quick-fixes for inspection warnings and errors |
| ++ctrl+slash++ | Toggle line comment | |
| ++ctrl+shift+slash++ | Toggle block comment | |

#### Generating Javadoc from the Shortcut

There is no default shortcut for Generate Javadoc. If you want one,
assign it yourself — it will persist in your keymap and sync to your
other devices via Settings Sync.

1. Open **File > Settings** (++ctrl+alt+s++).
2. Navigate to **Keymap**.
3. Search for `Generate JavaDocs for current element` in the
   action list.
4. **Right-click** the action and select **Add Keyboard Shortcut**.
5. Press your desired key combination and click **OK**.

!!! tip
    Before assigning a shortcut, check whether your chosen combination
    is already in use. IntelliJ IDEA will show a conflict warning in the
    keyboard shortcut dialog if it is.

### Code Analysis

| Shortcut | Action | Notes |
|---|---|---|
| ++f2++ | Jump to next error or warning | Cycles through inspection findings in the current file |
| ++shift+f2++ | Jump to previous error or warning | |
| ++ctrl+alt+shift+i++ | Run inspection by name | Run a specific inspection on demand |
| ++alt+enter++ | Show context actions | See suggested fixes for the highlighted issue |

### Refactoring

| Shortcut | Action | Notes |
|---|---|---|
| ++ctrl+alt+shift+t++ | Open Refactor menu | Access all refactoring options |
| ++shift+f6++ | Rename | Renames a variable, method, or class and updates every reference |
| ++ctrl+alt+m++ | Extract method | Extracts selected code into a new method |
| ++ctrl+alt+v++ | Introduce variable | Extracts an expression into a named local variable |

## Importing the CST Keymap

The CST keymap file is available in the
[`/resources/keymaps`](https://github.com/KJAlloway/COMM2216_User_Documentation_Project_KJA_DLN/tree/main/resources/keymaps)
folder of this repository.

!!! warning
    Importing a keymap does not overwrite your existing keymaps. You
    can switch back to any predefined keymap at any time using the
    dropdown in **File > Settings > Keymap**.

1. Download `CST_Keymap.xml` from the `/resources/keymaps` folder
   of this repository.

2. Open **File > Settings** (++ctrl+alt+s++).

3. Navigate to **Keymap**.

4. Click the **gear icon** (⚙) beside the keymap dropdown.

5. Select **Import Keymap**.

6. Navigate to the downloaded `CST_Keymap.xml` file and click **Open**.

    At this point, **CST_Keymap** will appear in the keymap dropdown.

7. Select **CST_Keymap** from the dropdown to make it active.

8. Click **OK** to save and close.

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
- Your settings sync across devices via your JetBrains account
- Your inspection profile provides live feedback aligned with course
  style requirements
- Recommended plugins are installed, including CheckStyle-IDEA for
  pre-submission verification
- Your keymap is configured with shortcuts optimised for your workflow

If you run into problems at any point, see the
[Troubleshooting Guide](troubleshooting.md).
