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

For example, if we're using the default welcome message:

```
<color="0055ff">Welcome to <b>{2}</>, {1}.</>
```

...a player is named *BrickBot* and the server name is *Funhouse*...
this welcome message will display as:

> <p style="color:#0055ff;">Welcome to **Funhouse**, BrickBot.<p>

### Self Damage

**:lucide-undo-2: Default: True**{.info-mini}

Option to toggle the player being able to damage themselves
outside of [minigames]() in the server.

By default, it is enabled. This does **not** mean that players can
hurt other players. It just means that players can use weapons on
themselves, therefore damaging themselves.

Disabling this grants all players immunity from projectiles
of their own weapons or explosives in the server.

### Physics Damage

**:lucide-undo-2: Default: False**{.info-mini}

Physics damage refers to high-speed impact, where if you do something like flying
and hit a wall, you will recieve some damage or even die. In this case, all
physics damage can be enabled or disabled with this setting outside of minigames.

### Enable Camera Blocked Effects

**:lucide-undo-2: Default: False**{.info-mini}

"Camera Blocked Effects" refers to an overlay that activates everytime
your character's camera intersects with the inside of an object. This overlay
serves as an obstruction to prevent you looking through bricks that are visible
but don't have collision with faces, that are culled.

## Applicator Limits

### Enforce Applicator Limits

**:lucide-undo-2: Default: False**{.info-mini}
[:lucide-shield-check: Can be bypassed with **Bypass Applicator Limits**](){.info-link-mini}

When enabled, acts as some sort of server wide clamp for components. Without the
Bypass Applicator Limits permission, the player will not be able to set
values beyond the slider limits of component parameters.

Intended for servers that are equivalent to a freebuild, where anyone can build
anywhere.

## Prefab Limits

Settings relating to the usage of prefabs in the server.

### Max Size

**:lucide-undo-2: Default: 100 × 100 × 100**{.info-mini}
[:lucide-shield-check: Can be bypassed with **Bypass Prefab Limits**](){.info-link-mini}

The maximum size of prefab on all 3 axes, using units of studs.

* **X:** Maximum size based on the first horizontal axis.
* **Y:** Maximum size based on the second horizontal axis.
* **Z:** Maximum size based on the vertical axis.

It is recommended to make X and Y equal to each other.
This will account for extra horizontal rotation.
By default, this is set to 100 studs in all axes.

### Max Bricks

**:lucide-undo-2: Default: 1000**{.info-mini}
[:lucide-shield-check: Can be bypassed with **Bypass Prefab Limits**](){.info-link-mini}

The maximum brick count allowed for prefabs.

### Max Components

**:lucide-undo-2: Default: 20**{.info-mini}
[:lucide-shield-check: Can be bypassed with **Bypass Prefab Limits**](){.info-link-mini}

The maximum component count allowed for prefabs.
Bricks that come with components attached also count towards
this limit.

### Upload Timeout

**:lucide-undo-2: Default: 5 seconds**{.info-mini}
[:lucide-shield-check: Can be bypassed with **Bypass Prefab Timeout**](){.info-link-mini}

Everytime a player uploads a prefab, enforce a delay temporarily
to prevent spamming prefabs. Unit is in seconds.

Set to 0s for no delay, but this can cause problems if you run
a public server. It is much easier to spam prefabs without a delay.

## Selector Limits

Settings related to controlling limits that are associated with the Selector.

### Max Selection Size

**:lucide-undo-2: Default: 100 × 100 × 100**{.info-mini}
[:lucide-shield-check: Can be bypassed with **Bypass Selector Limits**](){.info-link-mini}

The maximum size of a selection that can be made by a player
on all 3 axes, using units of studs.

* **X:** Maximum size based on the first horizontal axis.
* **Y:** Maximum size based on the second horizontal axis.
* **Z:** Maximum size based on the vertical axis.

It is recommended to make X and Y equal to each other.
This will account for extra horizontal rotation.
By default, this is set to 100 studs in all axes.

### Max Selected Bricks

**:lucide-undo-2: Default: 1,000**{.info-mini}
[:lucide-shield-check: Can be bypassed with **Bypass Selector Limits**](){.info-link-mini}

Maximum selected bricks per current selection. This
prevents people from making overly large selections.

### Selection Timeout

**:lucide-undo-2: Default: 2 seconds**{.info-mini}
[:lucide-shield-check: Can be bypassed with **Bypass Selector Timeout**](){.info-link-mini}

Enforce a delay temporarily upon the player after selecting
with the Selector. Unit is in seconds.

## Builder Limits[^1]

Settings related to controlling limits that are associated with the Builder.

!!! note

    The placer is hard-coded to only place 1,000 of an object at a time.

    While the max placement limits do not function beyond 1,000 copies
    of a single brick or entity, they are enforced upon pasting templates.

### Max Placement Bricks

**:lucide-undo-2: Default: 2000**{.info-mini}

Maximum number of bricks in a single placement.

### Max Placement Entities

**:lucide-undo-2: Default: 10**{.info-mini}

Maximum number of entities in a single placement.

### Template Placement Timeout

**:lucide-undo-2: Default: 2 seconds**{.info-mini}

Everytime a player places a template, enforce a delay temporarily
to prevent spamming the Builder. Unit is in seconds.

Set to 0s for no delay, but this can cause problems if you run
a public server. It is much easier to spam the Builder without a delay.

### Max Physics Objects

**:lucide-undo-2: Default: 2000**{.info-mini}

Maximum amount of physics objects **across the server.**

### Max Physics Objects per Player

**:lucide-undo-2: Default: 50**{.info-mini}

Maximum amount of physics objects **per player.**

## Auto Saving

Settings related to control of the auto-saver.

### Enable Auto Saves

**:lucide-undo-2: Default: False**{.info-mini}

Enables auto-saving of the world you're hosting on, given it is saved for the
first time to the Worlds directory.

For the autosave to trigger, it must detect changes or modifications in the
world. Otherwise, the autosave will not occur.

Manually saving on your end will not affect the timing of auto-saves.

### Enable Announcements

**:lucide-undo-2: Default: True**{.info-mini}

Displays messages in chat about autosaves including their statistics. You
can disable this if it becomes annoying or legitimately gets into the way of
chatting. The auto-saving will continue to run regardless if announcements
are enabled or not.

### Enable Screenshots

**:lucide-undo-2: Default: False**{.info-mini}

Captures a new thumbnail from your view for the world when it gets autosaved.
The old one will be overwritten on. Generally useful for documenting how far
you have gotten with your progress on a world and picking up where you left off.

Disable this to prevent the current thumbnail being overwritten if you already
have one saved manually with the world.

Thumbnails are not supported on [Dedicated servers]().

### Save Interval

**:lucide-undo-2: Default: 5 minutes**{.info-mini}

Controls how frequently the auto-saving occurs in minutes.

You may take into account the storage of your devices. The balance lies in
the way people play on the server. If stuff builds up fast over weeks, it may
be recommended to go for a longer autosave interval.

[^1]: I specifically call this section "Builder Limits" instead of "Placer Limits" because at some point I feel like they forgot that the Placer was renamed in the Builder.
