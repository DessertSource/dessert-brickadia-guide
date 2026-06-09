---
search:
  exclude: true
---

To save a new preset, click on the **:material-download: Save New Preset**{.button} button.

This will prompt you to type a name for a preset. After typing the name, press ++enter++ to save your current configuration as a preset. Clicking outside the name input box will discard creation of a new preset.

Clicking on a preset in the presets list will load it in its entirety.

The **:material-arrow-u-left-top: Defaults**{.button} button resets everything to default settings.

### Managing preset files

To manage preset files, hover over their names. The following actions are available:

- The pencil button **:material-pencil:**{.button .tiny} allows you to **rename** the preset.<br>
Type the new name for your preset and press ++enter++ to finish renaming the preset.
- The yellow overwrite button **:material-download:**{.button .tiny .yellow} allows you to **overwrite** a preset.<br>
To confirm overwriting the preset, click the **:material-download: Confirm Overwrite**{.button .yellow} button.
- The trash can button **:material-delete:**{.button .tiny .red} allows you to **delete** a preset.<br>
To confirm deleting the preset, click the **:material-delete: Confirm Deletion**{.button .red} button.

### Presets folder

The folder button **:material-folder:**{.button .tiny} opens the location of the game's presets folder in your operating system's file explorer. You can manage presets using conventional file explorer actions. All presets (palettes, avatars, environment settings and etc.) are in this directory:

=== "Windows"

    ``` toml
    C:\Users\[username]\AppData\Local\Brickadia\Saved\Presets\ # (1)!
    ```

    1. Remember to use the back slash (`\`)!

=== "Linux"

    ``` toml
    ~/.config/Epic/Brickadia/Saved/Presets/ # (1)!
    ```

    1. Remember to use the forward slash (`/`)!

!!! warning "Folders not supported"

    There is currently no interface and indexing for folders. You will not be able to grab presets inside folders.
