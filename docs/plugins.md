# Installing and Configuring Plugins

## Overview

Plugins extend IntelliJ IDEA's built-in functionality. While IDEA includes
strong support for Java and Kotlin out of the box, several plugins will
improve your experience in CST courses by automating repetitive formatting
tasks, enforcing documentation standards, running course-required code
analysis, and helping you build keyboard shortcut habits as you work.

This section covers the plugins recommended for CST students, explains
what each one does, and walks you through installing and configuring them.

By the end of this section, the recommended plugins will be installed and
active globally across all your IntelliJ IDEA projects.

!!! note
    Plugins are global to your IntelliJ IDEA installation — they apply
    to every project you open. If you enabled Settings Sync in
    [Installation and Student Account Setup](installation.md), installing
    a plugin on one device will make it available on all your synced
    devices automatically.

## Recommended Plugins for CST Students

| Plugin | Purpose |
|---|---|
| [CheckStyle-IDEA](https://plugins.jetbrains.com/plugin/1065-checkstyle-idea) | Runs the course Checkstyle ruleset against your code and reports violations in a dedicated panel |
| [Save Actions X](https://plugins.jetbrains.com/plugin/22113-save-actions-x) | Automatically reformats code and organizes imports every time you save a file |
| [JavaDoc](https://plugins.jetbrains.com/plugin/7157-javadoc) | Generates Javadoc comment stubs for classes, methods, and fields with a single shortcut |
| [GitToolBox](https://plugins.jetbrains.com/plugin/7499-gittoolbox) | Displays inline Git blame annotations and branch status directly in the editor |
| [Rainbow Brackets](https://plugins.jetbrains.com/plugin/10080-rainbow-brackets) | Colours matching bracket pairs to make nested code easier to read |
| [Key Promoter X](https://plugins.jetbrains.com/plugin/9792-key-promoter-x) | Displays the keyboard shortcut for any action you perform with the mouse, helping you learn shortcuts as you work |

## Installing a Plugin

The steps below apply to any plugin. Use them to install each plugin in
the table above.

1. Open **File > Settings** (++ctrl+alt+s++).

2. Select **Plugins** from the left panel.

3. Click the **Marketplace** tab at the top of the Plugins panel.

4. **Type** the name of the plugin in the search field.

5. Click **Install** next to the plugin name in the search results.

    At this point, IntelliJ IDEA will download and install the plugin.
    A progress bar will appear while the download completes.

6. Click **OK** when prompted to restart IntelliJ IDEA.

    At this point, the IDE will restart and the plugin will be active
    across all your projects.

!!! tip
    Install all recommended plugins before restarting. You can queue
    multiple installs and restart once to apply them all at the same time.

## Configuring CheckStyle-IDEA

### What Checkstyle Does

IntelliJ IDEA's built-in inspections give you live feedback as you type —
the red and yellow underlines you see in the editor. Checkstyle is a
separate tool that does something different: it runs a precise, shared
ruleset against your finished code and reports any violations in its own
panel.

The distinction matters because your instructors use Checkstyle to grade
your submissions. When your instructor runs the course Checkstyle XML
against your code, they see exactly the same results you do locally —
which means a clean Checkstyle run before you submit is a reliable signal
that your code meets the style requirements.

In short: IntelliJ inspections catch issues early while you write.
Checkstyle is the final check that matches exactly what your instructor runs.

!!! warning
    Checkstyle does not produce live underlines as you type. It runs
    on demand from the Checkstyle tool window. Do not assume a clean
    editor means a clean Checkstyle run — always check the Checkstyle
    panel before submitting.

### Loading the Course Checkstyle Configuration

Your instructor provides a Checkstyle XML configuration file with each
course lab template. You need to load this file into the CheckStyle-IDEA
plugin so it runs the correct rules.

1. Obtain the `COMP-2522-Checkstyle.xml` file from your course lab
   repository, or download it from the
   [`/resources`](https://github.com/KJAlloway/COMM2216_User_Documentation_Project_KJA_DLN/tree/main/resources)
   folder of this guide.

2. Open **File > Settings** (++ctrl+alt+s++).

3. Navigate to **Tools > Checkstyle** in the left panel.

4. Under **Configuration File**, click the **+** button to add a new
   configuration.

5. In the dialog that opens, select **Use a local Checkstyle file**.

6. Click **Browse** and navigate to your `COMP-2522-Checkstyle.xml`
   file.

7. Give the configuration a description, such as `COMP 2522`, and
   click **Next**.

8. Click **Finish**, then check the box next to your new configuration
   to make it active.

9. Click **OK** to save and close.

    At this point, the Checkstyle panel at the bottom of the IDE will
    use the course configuration when it runs.

### Confirming the Scan Scope

After loading the configuration, confirm it will run against your entire
project rather than a limited scope.

1. Open **File > Settings** (++ctrl+alt+s++).

2. Navigate to **Tools > Checkstyle**.

3. Locate the **Scan Scope** dropdown and confirm it is set to
   **All files** or your preferred scope.

    The Checkstyle configuration itself is stored globally in your IDE
    settings — you do not need to repeat the loading steps for each
    new project.

### Running Checkstyle

Once configured, you can run Checkstyle against your code at any time
from the Checkstyle tool window.

1. Open the Checkstyle tool window by clicking **Checkstyle** in the
   bottom toolbar, or navigate to **View > Tool Windows > Checkstyle**.

2. In the Checkstyle panel, click the **Check Current File** button
   (the green play icon) to run against the file you have open.

    Alternatively, click **Check Project** to run against all files
    in your project.

    At this point, any violations will appear as a list in the
    Checkstyle panel. Each entry shows the rule that was violated,
    the line number, and a description.

3. **Double-click** any violation in the list to jump directly to
   that line in the editor.

!!! tip
    Run **Check Current File** frequently as you work, not just before
    submission. Fixing one Checkstyle violation at a time is much faster
    than addressing a full list at the end.

### Common Checkstyle Violations in COMP 2522

| Violation | Cause | Fix |
|---|---|---|
| Missing Javadoc | A public class, method, or field is missing a Javadoc comment | Add a `/** */` comment with required tags above the element |
| Missing `@author` or `@version` | Class Javadoc exists but is missing required tags | Add `@author YourName` and `@version 1.0` to the class comment |
| Magic number | A numeric literal is used directly instead of a named constant | Assign the value to a `static final` constant and use the constant name |
| Line too long | A line exceeds 100 characters | Break the line using **Reformat Code** (++ctrl+l++) |
| Unused import | An import statement is present but not used in the file | Remove it, or use Save Actions X to remove it automatically on save |
| Trailing whitespace | A line ends with one or more spaces | Enable **Trim trailing whitespace** in Save Actions X settings |
| Missing `final` on parameter | A method parameter is not declared `final` | Add the `final` keyword before each parameter type |

## Configuring Save Actions X

Save Actions X runs a set of cleanup actions on your file automatically
each time you save. For CST coursework, the most useful actions are
reformatting your code, removing unused imports, and trimming trailing
whitespace — all things that Checkstyle checks and that are easy to
forget to do manually.

!!! warning
    Save Actions X modifies your file on every save. If you are working
    in a shared repository, confirm with your team that everyone is using
    the same code style settings before enabling reformatting, to avoid
    noisy diffs.

1. Open **File > Settings** (++ctrl+alt+s++).

2. Navigate to **Tools > Actions on Save** in the left panel.

3. Enable the following actions:

    - **Reformat code** — applies your code style settings to the
      entire file on every save
    - **Optimize imports** — removes unused imports and organizes
      import statements according to your code style settings

4. Click **OK** to save and close.

    At this point, every time you press ++ctrl+s++ or the IDE autosaves,
    your file will be automatically reformatted and its imports cleaned up.

!!! tip
    Save Actions X uses the code style settings configured at
    **File > Settings > Editor > Code Style**. If you have imported
    the CST inspection profile from [Configuring Inspections](inspections.md),
    your formatting will already match course style requirements.

## Configuring the JavaDoc Plugin

The JavaDoc plugin generates comment stubs for classes, methods, and
fields based on their signatures. Instead of typing `@param`, `@return`,
and `@throws` tags manually, the plugin inserts them for you and leaves
the description blank for you to fill in.

In CST courses, complete Javadoc comments are a standard requirement
for submitted code. This plugin significantly reduces the time it takes
to document your work correctly.

### Generating Javadoc for a Selected Element

1. Place your cursor on the class, method, or field you want to document.

2. Press ++alt+insert++ to open the **Generate** menu.

3. Select **Generate JavaDocs for selected element**.

    At this point, a Javadoc comment stub is inserted directly above
    the element. It includes `@param` tags for each parameter, a
    `@return` tag if the method returns a value, and `@throws` tags
    for any declared exceptions.

4. Fill in the description text for each tag.

### Generating Javadoc for an Entire File

1. Open the file you want to document.

2. Press ++ctrl+shift+a++ to open **Find Action**.

3. Type `Generate JavaDocs for all elements` and press ++enter++.

    At this point, stubs are inserted for every undocumented class,
    method, and field in the file.

!!! note
    The JavaDoc plugin only generates stubs — it does not write
    descriptions for you. You are responsible for filling in meaningful
    content for each tag. Javadoc comments with empty or placeholder
    descriptions will not satisfy course requirements.

## Configuring Key Promoter X

Key Promoter X requires no additional configuration to begin working.
Once installed, it will automatically display a popup in the bottom-right
corner of the IDE whenever you use the mouse to perform an action that
has a keyboard shortcut.

To adjust how often popups appear:

1. Open **File > Settings** (++ctrl+alt+s++).

2. Navigate to **Key Promoter X** in the left panel.

3. Adjust the **Suppress count** value — this controls how many times
   you can perform an action with the mouse before Key Promoter X stops
   reminding you about its shortcut.

## Conclusion

Your recommended plugins are now installed and configured globally across
all your IntelliJ IDEA projects. CheckStyle-IDEA will let you run the
course Checkstyle configuration before every submission. Save Actions X
will keep your code formatted and your imports clean automatically. The
JavaDoc plugin will reduce the time it takes to document your work. Key
Promoter X will help you build shortcut habits as you work through the
rest of this guide.
