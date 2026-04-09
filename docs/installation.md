# Installation and Student Account Setup

## Overview

This section walks you through installing IntelliJ IDEA on your computer,
activating a free JetBrains Education licence using your BCIT student email,
and enabling [settings sync](glossary.md#settings-sync) so your configuration
is consistent across multiple devices.

By the end of this section you will have a fully licensed, running copy of
IntelliJ IDEA linked to your JetBrains account, with global settings sync
active so every configuration change you make in the following sections
applies across all your devices automatically.

!!! note
    JetBrains offers the full IntelliJ IDEA Ultimate edition free to students
    at accredited institutions. Your BCIT email address (`@my.bcit.ca`)
    qualifies you automatically. You do not need a credit card.

## Downloading IntelliJ IDEA

1. Navigate to the [IntelliJ IDEA download page](https://www.jetbrains.com/idea/download/).

2. Select your operating system using the tabs at the top of the page:
   **Windows**, **macOS**, or **Linux**.

3. Under the **IntelliJ IDEA Ultimate** column, click **Download**.

    At this point, a `.exe` installer (Windows), `.dmg` disk image (macOS),
    or `.tar.gz` archive (Linux) will begin downloading.

!!! tip
    Download Ultimate, not Community. Ultimate is free with your student
    licence and includes features you will need in later CST terms,
    including database tools and Spring framework support.

## Installing IntelliJ IDEA

=== "Windows"

    1. Open the downloaded `.exe` installer.
    2. Click **Next** through the welcome screen.
    3. Select your installation directory and click **Next**.
    4. Under **Installation Options**, check **Add "Open Folder as Project"**.
    5. Click **Next**, then **Install**.
    6. Click **Finish** when the installation completes.

=== "macOS"

    1. Open the downloaded `.dmg` file.
    2. **Drag** the IntelliJ IDEA icon into your **Applications** folder.
    3. Open **Applications** and double-click **IntelliJ IDEA** to launch it.

=== "Linux"

    1. Extract the downloaded `.tar.gz` archive to your preferred location:
       ```
       tar -xzf ideaIU-*.tar.gz
       ```
    2. Navigate into the extracted folder and run:
       ```
       ./bin/idea.sh
       ```

## Activating Your Student Licence

JetBrains verifies student status through your institutional email address.
You will apply for a licence through the JetBrains website before activating
it inside the [IDE](glossary.md#ide).

!!! warning
    You must use your BCIT student email (`firstname_lastname@my.bcit.ca`)
    to qualify for the free Education licence. Personal email addresses
    are not eligible.

### Applying for a JetBrains Education Licence

1. Navigate to the [JetBrains Education licence page](https://www.jetbrains.com/community/education/#students).

2. Click **Apply Now**.

3. Fill in the application form:
    - Set **Apply with** to **University email address**
    - Enter your BCIT student email address
    - Complete the remaining fields with your name and institution

4. Click **Apply for Free Products**.

    At this point, JetBrains will send a confirmation email to your BCIT
    address. Check your inbox — it typically arrives within a few minutes.

5. Open the confirmation email and click **Confirm Request**.

    At this point, you will be redirected to create a
    [JetBrains account](glossary.md#jetbrains-account). Use your BCIT email
    address as your account email.

6. Set a password for your JetBrains account and click **Save**.

    Your Education licence is now active and linked to your JetBrains account.

### Activating the Licence in IntelliJ IDEA

1. Launch IntelliJ IDEA.

2. On the welcome screen, click **Activate IntelliJ IDEA**.

3. Select **Log in to JetBrains Account**.

4. Enter the email and password for your [JetBrains account](glossary.md#jetbrains-account)
   and click **Log In**.

    At this point, IntelliJ IDEA will detect your Education licence
    automatically and activate.

5. Click **Continue** to proceed to the IDE.

## Syncing Settings Across Devices

IntelliJ IDEA can sync your global [IDE](glossary.md#ide) settings — including
[keymaps](glossary.md#keymap), colour schemes, inspection profiles, and
[plugin](glossary.md#plugin) configurations — to your JetBrains account so
they are available on any device you log into.

!!! warning
    [Settings sync](glossary.md#settings-sync) only pushes your **global IDE
    settings**. Project-specific overrides — such as an inspection profile
    stored at the project [scope](glossary.md#scope-ide-settings) rather than
    the IDE level — are not synced. As you work through the following sections,
    each page will confirm that the settings you configure are stored globally
    so they sync correctly.

!!! tip
    Enable settings sync now, before you configure anything else in this
    guide. This ensures that every configuration change you make in the
    following sections is automatically available on all your devices
    without any additional steps.

1. Open **File > Settings** (++ctrl+alt+s++).

2. Navigate to **Tools > Backup and Sync** in the left panel.

3. Click **Enable Settings Sync**.

4. Select the categories you want to sync. For CST coursework, enable:
    - **UI Settings**
    - **Keymaps**
    - **Code**
    - **Plugins**

5. Under the sync scope option, select **Sync only this IDE** to keep
   your IntelliJ IDEA settings separate from other JetBrains IDEs, or
   select **Sync all JetBrains IDEs** if you use other JetBrains tools
   and want a shared configuration.

6. Click **Sync** to upload your current settings to your JetBrains account.

    At this point, your IDE settings are stored in your JetBrains account
    and will be pushed to any other device where you log in with the same
    account.

## Conclusion

At this point, IntelliJ IDEA is installed, licenced, and synced to your
JetBrains account. Your global settings will now follow you across devices
automatically.

Verify your setup before continuing:

- IntelliJ IDEA launches without a trial or activation prompt
- The title bar does not display "— (evaluation copy)"
- **Help > About** shows your licence as **For educational use only**
