---
icon: material/console-line
---

# Chat Commands

This page contains all chat commands available by default in Brickadia.
These commands are not case sensitive.
You can use quotes ("") if the parameter has spaces.

Chat commands that are done outside of the /help list are added and
interpreted by external server tools like Omegga.

## `/help`

Shows the list of Brickadia's default commands and their descriptions.

**Variations:**

* `/help [Command]` - Get information for the specified command.

## `/tp`

Teleports you to different locations depending on the arguments
you give the command.

Without arguments, you yourself will be teleported to where your
crosshair is aiming at. (The crosshair must point at a solid object.)

**Variations:**

* `/tp "Destination Player"`
    * **Destination Player:** The player to teleport to.
* `/tp "Target Player" "Destination Player"`
    * **Target Player:** The player that will be teleported by this command.
    * **Destination Player:** The player to teleport to.<br>
* `/tp "Target Player" [X] [Y] [Z] [Keep Velocity]`
    * **Target Player:** The player that will be teleported by this command.
    * **X:** X (horizontal X axe) coordinate for the destination.
    * **Y:** Y (horizontal Y axe) coordinate for the destination.
    * **Z:** Z (vertical) coordinate for the destination.
    * **Keep Velocity:** Self explanatory.
    0 removes all velocity. 1 keeps velocity.
* `/tp "Target Player" [X] [Y] [Z] [Pitch] [Yaw] [Keep Velocity]`
    * Everything is almost the same, aside from the Pitch and Yaw arguments.
        * **Pitch:** Horizontal player rotation *(This does not actually
        work, but is required.)*
        * **Yaw:** Vertical player rotation.

## `/back`

Teleports you back to the last location you were teleported from.

**Variations:**

* `/back [Target Player]`
    * **Target Player:** Teleports the specified players back to where
    *they* were teleported from.

## `/getTransform`

Get your location and rotation in numerical values. Useful for inputting into
a Teleport gate or writing them down for future design reference.

**Variations:**

* `/getTransform [Target Player]`
    * **Target Player:** Get location and rotation from the specified player.

## `/load`

Load a legacy prefab file additively to the world.

!!! note
    This will not load a save file as a prefab! It will load legacy prefab
    saves directly into the world.

* `/load "File" [X Offset] [Y Offset] [Z Offset]`
    * **File:** The legacy prefab file to load.
    * **X Offset:** X (horizontal X axe) offset from the world center.
    * **Y Offset:** Y (horizontal Y axe) offset from the world center.
    * **Z Offset:** Z (vertical) offset from the world center.
* `/load "File" [X Offset] [Y Offset] [Z Offset] [Palette Color Correction] [Custom Color Correction]`
    * Everything is almost the same, aside from the color correction arguments.
        * **Palette Color Correction:** Apply corrections to the loaded prefab
        based on palette colors. 0 is False and 1 is True.
        * **Custom Color Correction:** Whether or not to apply the same
        correction above to custom colors. 0 is False and 1 is True.

## `/clearAllBricks` :material-alert-octagon-outline:

Clears **all** bricks and entities.

!!! danger

    This command must be used only when everyone in the server is aware
    of what you're doing and have dealt with the repercussions!

## `/clearBricks`

Clears *your own* bricks and entities.

**Variations:**

* `/clearBricks [Player]`<br>
Clears the specified player's bricks and entities.

## `/brickCount`

Get the count of all bricks in the server including those on brick grids.

## `/playerCount`

Get the count of all players in the server.

## `/listPlayers`

List all players' names in the server.

## `/listRoles`

List all roles in the server.

## `/listTeams`

List all teams in the current minigame you are in.
