---
icon: lucide/server-cog
tags:
    - Server Management
---

# Advanced Server Settings

## In-Game

### Welcome Message

Message to show players upon joining the server.

This can be set to a single line of text with support for:

* Regular formatting (**bold**, *italics*, color, etc...)
* Fetching the current server name (type in `{2}`)
* Fetching the player's name (type in `{1}`)

### Self Damage

Option to toggle the player being able to damage themselves
outside of [minigames]() in the server.

By default, it is enabled. This does **not** mean that players can
hurt other players. It just means that players can use weapons on
themselves, therefore damaging them.

Disabling this grants all players immunity from projectiles
of their own weapons or explosives in the server.

### Physics Damage

Physics damage refers to high-speed impact, where if you do something like flying
and hit a wall, you will suffer some damage or even die. In this case, all
physics damage can be enabled or disabled with this setting outside of minigames.

By default, this is disabled for the obvious reason that
it would be very annoying to build and fly around with it on.
Imagine you kept having to conservatively fly around your build like some sort
of obby. Not very pleasant nor adjacent to the spirit of creation.

### Enable Camera Blocked Effects

"Camera Blocked Effects" refers to an overlay that activates everytime
your character's camera intersects with a brick that has collision enabled.
This overlay serves as an obstruction to prevent you looking through bricks.

This is disabled for another obvious reason: Having the screen
reverse flashbang everytime you work on a project isn't ideal. Imagine
your monitor shuts off constantly and turns back on in variable intervals.
It's very distressing to think about.

## Applicator Limits

### Enforce Applicator Limits

When enabled, acts as some sort of server wide clamp for components. Without the
[Bypass Applicator Limits]() permission, the player will not be able to set
values beyond the slider limits of component parameters.

## Prefab Limits

### Max Size

### Max Bricks

### Max Components

### Upload Timeout

## Selector Limits

### Max Selection Size

### Max Selected Bricks

### Selection Timeout

## Placer Limits

### Max Placement Bricks

### Max Placement Entities

### Template Placement Timeout

### Max Physics Objects

### Max Physics Objects per Player

## Auto Saving

### Enable Auto Saves

Enables auto-saving of the world you're playing on, given it is saved for the
first time to the Worlds directory.

For the autosave to trigger, it must detect changes or modifications in the
world. Otherwise, the autosave will not occur.

### Enable Announcements

Displays messages in chat about autosaves including their statistics. You
can disable this if it becomes annoying or legitimately gets into the way of
chatting. The auto-saving will continue to run regardless if announcements
are enabled or not.

### Enable Screenshots

Captures a new thumbnail for the world when it gets autosaved. The old one will
be overwritten on. Generally useful for documenting how far you have gotten with 
your progress on a world and picking up where you left off.

Disable this to prevent the current thumbnail being overwritten if you already have one saved manually with the world.

Thumbnails are not supported on [Dedicated servers]().

### Save Interval

Controls how frequently the auto-saving occurs in minutes. By default, this
is set to a reasonable 5 minutes.

You may take into account the storage of your devices. The balance lies in
the way people play on the server. If stuff builds up fast over weeks, it may
be recommended to go for a longer autosave interval.
