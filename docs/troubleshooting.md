# Troubleshooting

This page covers common problems encountered during the setup and
configuration tasks in this guide.

## IntelliJ IDEA Will Not Activate After Logging In

**Symptom:** After logging into your JetBrains account in the IDE,
IntelliJ IDEA still shows a trial or activation prompt.

**Solution:**

1. Confirm your Education licence is active by logging into
   [account.jetbrains.com](https://account.jetbrains.com) in a browser.
   Under **Licenses**, you should see **IntelliJ IDEA Ultimate —
   Educational**.
2. If the licence is listed but IDEA still will not activate, open
   **Help > Register** inside the IDE and log in again.
3. If your licence is not listed, your BCIT email may not have been
   recognised automatically. Visit the
   [JetBrains Education page](https://www.jetbrains.com/community/education/#students)
   and reapply using the **Official Document** tab, uploading a copy
   of your BCIT acceptance letter or student ID.

## The Confirmation Email from JetBrains Never Arrived

**Symptom:** After applying for an Education licence, no confirmation
email arrived at your BCIT address.

**Solution:**

1. Check your **Spam** or **Junk** folder in your BCIT email.
2. Wait up to 15 minutes — delivery to institutional email addresses
   can be delayed.
3. If the email still has not arrived, return to the
   [JetBrains Education application page](https://www.jetbrains.com/community/education/#students)
   and resubmit using the same email address.

## Settings Sync Is Not Working on a Second Device

**Symptom:** After logging into IntelliJ IDEA on a second computer,
your keymaps, plugins, or inspection profiles are not present.

**Solution:**

1. Open **File > Settings > Settings Sync** and confirm that sync
   is enabled and shows a recent sync timestamp.
2. Click **Sync** to force a manual sync.
3. If the categories you want are not syncing, check that they are
   checked under **File > Settings > Settings Sync**.

!!! warning
    Settings sync requires both devices to be running the same major
    version of IntelliJ IDEA. If one device is on an older version,
    update it first.

## The CST Inspection Profile Does Not Appear After Importing

**Symptom:** After importing `CST_Inspections.xml`, the profile name
does not appear in the Inspections dropdown.

**Solution:**

1. Confirm that the file downloaded completely and is not corrupted —
   it should be a valid XML file you can open in a text editor.
2. In **File > Settings > Editor > Inspections**, click the gear icon
   (⚙) and select **Import Profile** again.
3. If the import still fails, check that you are importing from
   **Editor > Inspections** and not from a different settings panel.

## The CST Inspection Profile Only Applies to One Project

**Symptom:** The `CST_Inspections` profile is active in one project
but does not appear, or reverts to the default, when you open a
different project.

**Cause:** The profile was imported while a project was open and was
stored at the project level rather than globally in your IDE settings.
It will show as `CST_Inspections (Project)` in the profile dropdown.

**Solution:**

1. Open **File > Settings** (++ctrl+alt+s++).
2. Navigate to **Editor > Inspections**.
3. Confirm the profile dropdown shows `CST_Inspections (Project)`.
4. Click the **gear icon** (⚙) at the top of the Inspections panel.
5. Select **Copy to IDE** from the dropdown.

    At this point, the profile is copied to your global IDE settings.
    The dropdown label will change to `CST_Inspections` without the
    `(Project)` suffix, and the profile will now apply to every project
    you open.

## A Plugin Fails to Install or Shows an Error After Installing

**Symptom:** A plugin download fails, or IntelliJ IDEA shows an error
after installing a plugin and restarting.

**Solution:**

1. Check your internet connection and retry the install from
   **File > Settings > Plugins > Marketplace**.
2. If the plugin installed but is causing errors, disable it without
   uninstalling: open **File > Settings > Plugins**, find the plugin,
   and toggle it off. Restart the IDE.
3. If problems persist, uninstall the plugin from the same panel and
   report the issue to your instructor.

## ++ctrl+alt+l++ Does Not Reformat Code on Windows

**Symptom:** Pressing ++ctrl+alt+l++ does not reformat code — the
screen locks instead.

**Cause:** On some Windows systems, ++ctrl+alt+l++ is assigned to
the system screen lock shortcut, which takes priority over the IDE.

**Solution:**

Use ++ctrl+l++ instead. This shortcut is included in the CST keymap
as a second binding for Reformat Code and does not conflict with any
Windows system shortcuts. If you have not yet imported the CST keymap,
see [Keyboard Shortcuts](shortcuts.md) for import instructions.

Alternatively, assign your own shortcut manually:

1. Open **File > Settings** (++ctrl+alt+s++).
2. Navigate to **Keymap**.
3. Search for **Reformat Code** in the action list.
4. **Right-click** **Reformat Code** and select **Add Keyboard Shortcut**.
5. Press your desired key combination and click **OK**.
