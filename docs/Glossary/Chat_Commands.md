---
icon: material/console-line
---

# Chat Commands

This page contains all chat commands available by default in Brickadia.
These commands are not case sensitive.
You can use quotes ("") if the parameter has spaces.

Chat commands that are done outside of the /help list are added and
interpreted by external server tools like Omegga.

## Help

### `/help`

Shows the list of Brickadia's default commands and their descriptions.

**Variations:**

* `/help [Command]` - Get information for the specified command.

## Teleportation

### `/tp`

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

### `/back`

Teleports you back to the last location you were teleported from.

**Variations:**

* `/back [Target Player]`
    * **Target Player:** Teleports the specified players back to where
    *they* were teleported from.

## Operations

### `/load`

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

### `/clearAllBricks`

Clears **all** bricks and entities.

!!! danger

    This command must be used only when everyone in the server is aware
    of what you're doing and have dealt with the repercussions!

### `/clearBricks`

Clears *your own* bricks and entities.

**Variations:**

* `/clearBricks [Player]`<br>
Clears the specified player's bricks and entities.

### `/DestroyAllGrids`

Clears **all** brick grids on the server.

!!! danger

    This command must be used only when everyone in the server is aware
    of what you're doing and have dealt with the repercussions!

## Statistics

### `/getTransform`

Get your location and rotation in numerical values. Useful for inputting into
a Teleport gate or writing them down for future design reference.

**Variations:**

* `/getTransform [Target Player]`
    * **Target Player:** Get location and rotation from the specified player.

### `/brickCount`

Get the count of all bricks in the server including those on brick grids.

### `/playerCount`

Get the count of all players in the server.

### `/listPlayers`

List all players' names in the server.

### `/listRoles`

List all roles in the server.

### `/Ping`

Prints "Pong!" in the chat for latency measuring purposes.

## Roles and Permissions

### `/grantRole`

Give a player the specified role.

**Arguments:**

* **"Role" (required):** Must be a role that exists in the server.
* **"Player" (required):** Must be the name of a player that you're giving
the role to.

**Usage example:**

```
/grantRole "nonbinary" "Dessert Source"
```

### `/revokeRole`

Give a player the specified role.

**Arguments:**

* **"Role" (required):** Must be the role that the player has.
* **"Player" (required):** Must be the name of a player that you're taking
away the role from.

**Usage example:**

```
/revokeRole "moderator" "Dessert Source"
```

## Moderation

### `/kick`

Kicks a player out of the server.

**Arguments:**

* **"Player" (required):** Name or UUID of the player to kick.
* **"Reason":** Optional reason for kicking that will be displayed
to player.

**Usage example:**

Kicking without reason:

```
/kick "Dessert Source"
```

Kicking with reason:

```
/kick "Dessert Source" "you smell"
```

Kicking without reason using UUID:

```
/kick 4b5c5489-b87f-4170-9970-96535fe20b19
```

Kicking with reason using UUID:

```
/kick 4b5c5489-b87f-4170-9970-96535fe20b19 "you smell"
```

### `/ban`

Bans a player for a specific time period.

**Arguments:**

* **"Player" (required):** Name or UUID of the player to ban.
* **[Time in minutes] (required):** How many minutes to ban this player
for. Here's a table that has pre-calculated times to ban a person for.

| Value  | Period               |
| ------ | -------------------- |
| -1     | Permanent            |
| 0      | Equivalent to a kick |
| 1      | 1 minute             |
| 60     | 1 hour               |
| 1440   | 1 day                |
| 10080  | 1 week               |
| 43800  | 1 month              |
| 525600 | 1 year               |

* **"Reason":** Optional reason for kicking that will be displayed
to player.

**Usage example:**

Banning without reason for 1 hour:

```
/ban "Dessert Source" 60
```

Banning with reason for 1 day:

```
/ban "Dessert Source" 1440 "you stink"
```

Banning with reason permanently:

```
/ban "Dessert Source" -1 "you are a melon"
```

Banning with reason using UUID permanently:

```
/ban 4b5c5489-b87f-4170-9970-96535fe20b19 -1 "you are a melon"
```

### `/unban`

Lift a ban off a player regardless of how long they have been banned for.

**Arguments:**

* **"Player" (required):** Name or UUID of the player to un-ban.

Unbanning with username:

```
/unban "Dessert Source"
```

Unbanning with UUID:

```
/unban 4b5c5489-b87f-4170-9970-96535fe20b19
```

## Minigame

### `/listTeams`

Lists all teams for the current minigame you're in.

### `/joinTeam`

Join an existing team in the current minigame you're in.

**Usage example:**

```
/JoinTeam "Trail Blazers"
```

### `/leaveTeam`

Leave your team in the current minigame you're in.

### `/clearCheckpoint`

Clear your selected checkpoint. Also works outside of minigames.

## Spectator

### `/spectator`

Toggles spectator mode. Your character will be hidden until this is off.
Not usable in minigames.

### `/spectate`

Spectate a specific player. Alternatively, turn off spectator mode when
no arguments are sent.

**Arguments:**

* **"Player" (required):** Name of the player to spectate. Leave blank
to disable spectator mode.

**Usage example:**

Spectate a player:

```
/spectate "Dessert Source"
```

Turn off spectator mode:

```
/spectate
```

## Autosave

### `/loadAutosave`

**Arguments:**

* **[Number] (n):** Load the *n^th^* last autosave. Leave blank to load
the last autosave.

**Usage example:**

Load last autosave:

```
/loadAutosave
```

Load the 6th last autosave:

```
/loadAutosave 6
```

### `/listAutosaves`

**Arguments:**

* **[Number] (n):** Lists the last *n* autosaves. Leave blank to list
the last 16 autosaves by default.

**Usage example:**

List the last 16 autosaves:

```
/listAutosaves
```

List the last 25 autosaves:

```
/listAutosaves 25
```

List the last 40 autosaves:

```
/listAutosaves 40
```
