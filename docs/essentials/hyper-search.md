---
icon: lucide/book-search
tags:
    - Essentials
---

# Hyper search

Press ++lctrl+b++ to open up the Hyper Search dialog. The hyper
search dialog can be used from anywhere provided you do not have
another menu open.

![Hyper search dialog](../assets/media/essentials/hyper-search/hyper-search-dialog.jpg)

Hyper search allows you to immediately find a specific item from
the Catalog. Start typing in the input box to find what you want in
the dialog. Clicking on an item found in hyper search will place it
in the temporary slot of your hotbar.

!!! Note

    Hyper search does not search for category, it only searches
    for the name of the items. If you were expecting something
    like `special` to show all bricks in the Special category
    and it does not, this is why.

## Hyper search filters

If hyper search is too cluttered when looking for a specific item,
you can use filters to make hyper search results more relevant to
your needs.

Hyper search only activates when you type at least one character
after typing the filter (example: `i:`) first. Only one filter can
be active at once. For example, `b: g:` will refuse to work.

### Brick filter (`b:`)

Type `b:` first into the input box to filter for bricks only.

Examples:

- `b:tile` returns tile bricks.
- `b:octo` returns octagonal shaped bricks.
- `b:button` returns buttons.

### Entity filter (`e:`)

Type `e:` first into the input box to filter for entities only.

Examples:

- `e:ball` returns the resizable ball.
- `e:wagon` returns both variants of the Wagon wheel.

### Gate filter (`g:`)

Type `g:` first into the input box to filter for gates only.

Examples:

- `g:array` returns array related gates.
- `g:teleport` returns teleportation related gates.
- `g:leaderboard` returns leaderboard related gates.

### Item filter (`i:`)

Type `i:` first into the input box to filter for items only.

Examples:

- `i:pistol` returns weapons with "Pistol" in their name.
- `i:soda` returns the Soda Can.

### Prefab filter (`p:`)

Type `p:` first into the input box to filter for prefabs only.

Examples:

- `p:house` returns prefabs with "House" in their name.
- `p:tree` returns prefabs with "Tree" in their name.
