# Troubleshooting

This page covers common problems encountered during the setup and 
configuration tasks in this guide.

## IntelliJ IDEA will not activate after logging in

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

## The confirmation email from JetBrains never arrived

**Symptom:** After applying for an Education licence, no confirmation 
email arrived at your BCIT address.

**Solution:**

1. Check your **Spam** or **Junk** folder in your BCIT email.
2. Wait up to 15 minutes — delivery to institutional email addresses 
   can be delayed.
3. If the email still has not arrived, return to the 
   [JetBrains Education application page](https://www.jetbrains.com/community/education/#students) 
   and resubmit using the same email address.

## Settings sync is not working on a second device

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

## The CST inspection profile does not appear after importing

**Symptom:** After importing `CST_Inspections.xml`, the profile name 
does not appear in the Inspections dropdown.

**Solution:**

1. Confirm that the file downloaded completely and is not corrupted — 
   it should be a valid XML file you can open in a text editor.
2. In **File > Settings > Editor > Inspections**, click the gear icon 
   (⚙) and select **Import Profile** again.
3. If the import still fails, check that you are importing from 
   **Editor > Inspections** and not from a different settings panel.

## A plugin fails to install or shows an error after installing

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

## ++ctrl+alt+l++ (Reformat Code) does not work on Windows

**Symptom:** Pressing ++ctrl+alt+l++ does not reformat code — the 
screen locks instead.

**Cause:** On some Windows systems, ++ctrl+alt+l++ is assigned to 
the system screen lock shortcut, which takes priority over the IDE.

**Solution:**

1. Open **File > Settings > Keymap**.
2. Search for **Reformat Code** in the action list.
3. Right-click **Reformat Code** and select **Add Keyboard Shortcut**.
4. Assign an alternative shortcut that does not conflict with your 
   system, such as ++ctrl+shift+alt+l++.
5. Click **OK** to save.