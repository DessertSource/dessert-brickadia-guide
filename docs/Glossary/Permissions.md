---
icon: material/shield-key-outline
---

# Permissions

There are three states for each individual permission in Brickadia:

* Allowed - Allow tools and features for player
* Forbidden - Disable tools and features for player
* Unchanged - Inherit the upper role's permission state between
*Allowed* or *Forbidden*

!!! Note

    These permission tags are here for reference, they are last
    minute additions without UX polish. They are used for the
    Set Player Permission gate.

## Always Leave Minigame

``` c
BR.Permission.AlwaysLeaveMinigame
```

Allows the player to leave the default minigame applied to them on join.

## Always Switch Team

``` c
BR.Permission.AlwaysSwitchTeam
```

Ignore all team balance restrictions in minigame. Allows the player
to be able to switch teams at all times.

## Ban

``` c
BR.Permission.Ban
```

Allows the player to ban players using either the command
or the player menu.

!!! warning

    Take care to grant this permission wisely. Do not give this
    permission to people you do not trust or are suspected of hiding 
    malicious intent.

## Building

``` c
BR.Permission.Building
```

Allows the player to build in the world.
Required for using build tools.

!!! Tip

    You can give a role that forbids this permission if they misbehave
    with the building tools.

### Use Applicator

``` c
BR.Permission.Building.Applicator
```

Allows the player to use the applicator.

#### Bypass Limits

``` c
BR.Permission.Building.Applicator.BypassLimits
```

Player will be able to override component limits set for the Applicator.

#### Edit Bricks

``` c
BR.Permission.Building.Applicator.EditBricks
```

Player will be able to modify bricks and component settings.

#### Edit Entities

``` c
BR.Permission.Building.Applicator.EditEntities
```

Player will be able to modify entities' settings.
