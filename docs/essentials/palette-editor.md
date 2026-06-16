---
icon: lucide/swatch-book
tags:
    - Essentials
    - Palettes
    - Presets
---

# Palette editor

![Palette editor](../assets/media/essentials/palette-editor/palette-editor.jpg)

The palette editor is where you edit palettes for use in the avatar editor or the server.

Menus that allow you to access the palette editor:

- [:lucide-shirt: Avatar editor](./avatar-editor.md)
- :lucide-server-cog: Server settings

!!! note

    You will not be able to undo changes to your palette, and you will lose all your changes without being prompted if you press ++esc++! Be careful.

## What is a palette?

![Various palettes](../assets/media/essentials/palette-editor/palettes.png){.borderless}

A palette is a set of colors that can be used for painting avatars or objects on a server. You are not required to sync the avatar and the server palette together.

There are limits to what each palette can contain per file:

- 16 groups
- 16 colors per group
- 256 colors per palette in a 16x16 grid

## Adding colors

Click the plus button **:material-plus:**{.button .tiny} below the existing colors to add a new color. The new color is white until edited.

![Button to add a new color](../assets/media/essentials/palette-editor/add-color.png)

## Moving colors

Click and drag colors to move them on the palette, across different color groups.
The line displays where your color group will be placed between.

![Dragging and dropping colors](../assets/media/essentials/palette-editor/drag-color.png)

## Editing colors

Click on a color to open the color picker window.

![Color picker window](../assets/media/essentials/palette-editor/edit-color.png)

The color picker window has the following elements:

On the left:

1. **Color wheel:** Controls the hue and saturation.
2. **Value slider:** Controls the value/brightness of the color.

On the right:

1. **RGB sliders:** Controls the percentage of red, green and blue that the color has.
2. **HSV sliders:** Controls the degree of hue, the percentage of saturation and the percentage of value that the color has.
3. **Hex code input:** You can import hex codes from HTML or creative software.

You can click off the color picker window once you are done with picking the color you want.

## Removing colors

Right click on a color to delete it from a column.

![A color being deleted](../assets/media/essentials/palette-editor/remove-color.png)

## Adding color groups

Click the plus button **:material-plus:**{.button .tiny} next to the existing groups to add a new color group.

![Button to add new color group](../assets/media/essentials/palette-editor/add-color-group.png)

If the button is greyed out  **:material-plus:**{.button .tiny .trans}, you have reached the maximum color group limit of 16 groups.

## Moving color groups

Click and drag the top part of a color group to move the color group.
The line displays where your color group will be placed between.

![Dragging and dropping palette color groups](../assets/media/essentials/palette-editor/drag-color-group.png)

## Naming color groups

Click on the top part of a color group to select that group.
Selecting that color group allows you to name the color group to suit their colors.

![Naming a color group](../assets/media/essentials/palette-editor/naming-color-group.png)

Keep them short but descriptive. Some good names for groups include:

- Grayscale
- Foliage
- Neon
- Metallic

## Removing color groups

Right click on the top dark part of a color group to delete it.

![A color group being removed](../assets/media/essentials/palette-editor/remove-color-group.png)

## Editing palette information

You can edit the description of your palette. You can describe what the palette is for. Some good details to add:

![alt text](../assets/media/essentials/palette-editor/palette-information.png)

- The creator of the palette
- Is the palette used for a server or the avatar editor
- A brief description of what the palette is good for

## Saving the palette

To save your changes of the palette directly onto the server or the avatar editor, click the **:material-arrow-right: Save**{.button .green} button.

### Migrating colors in a server

If you decide to save changes to the server palette,
this dialog will appear and ask you to migrate colors with one of these three methods.

![Color migration dialog](../assets/media/essentials/palette-editor/color-migration-dialog.png)

!!! bug

    There is currently a bug where non-brick grid entities do not migrate over.
    Anything with an asterisk indicates an incorrect result due to this bug.

=== ":lucide-arrow-right: Leave as is"

    All objects retain their color with this migration method, regardless of similarness and color order or index.

    New objects can be placed with the new colors and they still wouldn't affect the colors of old objects.

    A before/after is not needed. Everything is the same.

=== ":lucide-paint-bucket: Migrate to nearest"

    With this migration method,
    objects with non-existing colors will inherit the new colors closest to them,
    regardless of palette index.

    === "Before"

        ![Before migrating to nearest](../assets/media/essentials/palette-editor/migrate-to-nearest-before.jpg)

    === "After"

        ![After migrating to nearest](../assets/media/essentials/palette-editor/migrate-to-nearest-after.jpg)

=== ":lucide-paint-bucket: Migrate by index"

    This migration method does not match by color.
    Instead, it matches up against the index of the previous palette.
    If you change the layout of the palette, there's no guarantee any of the old colors will be retained.

    === "Before"

        ![Before migrating by index](../assets/media/essentials/palette-editor/migrate-by-index-before.jpg)

    === "After"

        ![After migrating by index](../assets/media/essentials/palette-editor/migrate-by-index-after.jpg)

## Palette presets

![Palette editor presets](../assets/media/essentials/palette-editor/palette-editor-presets.png)

--8<--
docs/snippets/shared/presets.md:6
--8<--
