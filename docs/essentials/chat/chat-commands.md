---
icon: lucide/terminal
tags:
    - Basics
---

# Chat Commands

A comprehensive list of commands you can send in the chat.

You can use "quotes" to pass string arguments.
Commands are not case-sensitive, so feel free to type commands lower-case as they still work.

!!! note

    Some chat commands may be made admin-only for safety reason on servers. Check your permissions.

## `/Help`

Displays all commands and their brief descriptions.

### Detailed command help

```
/Help [Command]
```

If you add the name of a command, it will also describe the command and its arguments in detail.

| Parameter | Type   | Description                      |
| --------- | ------ | -------------------------------- |
| Command   | String | Name of command to get help with |

``` title='Example: Getting detailed help for the /TP command'
/Help TP
```

## Informational commands

### `/BrickCount`

Shows the brick count for the entire world.

#### Brick count for specific player

```
/BrickCount [Player]
```

If you add a player name to the command, it shows a player's brick count.

| Parameter | Type   | Description                            |
| --------- | ------ | -------------------------------------- |
| Player    | String | Name of player to get brick count from |

``` title='Example: Getting the brick count of player named "Faker"'
/BrickCount "Faker"
```

### `/PlayerCount`

Shows the current number of players on the server.

### `/ListRoles`

Lists all roles inside the server in chat.

### `/GetTransform`

Displays your in-game location coordinates and rotation in the chat.

#### Getting another player's coordinates

```
/GetTransform [Target Player]
```

If you add a player name to the command, this displays in-game location coordinates and rotation of another player.

| Parameter     | Type   | Description                                        |
| ------------- | ------ | -------------------------------------------------- |
| Target Player | String | Name of player to get coordinate and rotation from |

``` title='Example: Getting the coordinates and rotation of a player named "Dad"'
/GetTransform "Dad"
```

### `/Ping`

Prints "Pong!" in the chat.
Used to measure if the server has latency.

If it takes a noticeable while to respond, the latency on the server is suboptimal.

## Minigame commands

### `/JoinTeam`

Joins the specified team inside the minigame you are in.

| Parameter         | Type   | Description          |
| ----------------- | ------ | -------------------- |
| Team *(required)* | String | Name of team to join |

``` title='Example: Joining the team "New York Knicks"'
/JoinTeam "New York Knicks"
```

### `/LeaveTeam`

Leave your current team inside the minigame you are in.

### `/ListTeams`

Lists all teams in the chat for the minigame you are in.

### `/KillAllBots`

Force self-destruct all bots in the server, which is most useful for minigames.

## Movement commands

### `/ClearCheckPoint`

Clears your current checkpoint.

### `/TP`

Teleports you based on where you're looking.

You must be looking at a visible object.
If you try to look at the sky and teleport, it will declare you are not looking at a visible object.

#### Teleporting to a player

```
/TP [Destination Player]
```

This teleports yourself to that player.

| Parameter          | Type   | Description                   |
| ------------------ | ------ | ----------------------------- |
| Destination Player | String | Name of player to teleport to |

``` title='Example: Teleporting yourself to a player named "Betz"'
/TP "Betz"
```

#### Teleporting a player to another player

```
/TP [Target Player] [Destination Player]
```

This teleports the target player to the other player.

| Parameter          | Type   | Description                   |
| ------------------ | ------ | ----------------------------- |
| Target Player      | String | Name of player to teleport    |
| Destination Player | String | Name of player to teleport to |

``` title='Example: Teleporting player "Bachelorette" to player "Vespertine"'
/TP "Bachelorette" "Vespertine"
```

#### Teleporting a player to a coordinate

```
/TP [Target Player] [X] [Y] [Z] [Keep Velocity]
```

Teleports a player to a specified location with coordinates in the world.

| Parameter     | Type    | Description                                                                  |
| ------------- | ------- | ---------------------------------------------------------------------------- |
| Target Player | String  | Name of player to teleport                                                   |
| X             | Number  | X coordinate of the destination, in micro-units                              |
| Y             | Number  | Y coordinate of the destination, in micro-units                              |
| Z             | Number  | Z coordinate of the destination, in micro-units                              |
| Keep Velocity | Boolean | Whether or not to retain velocity after teleporting<br>1 = true<br>0 = false |

``` title='Example: Teleporting player "Heathcliff" to a destination, retaining velocity'
/TP "Heathcliff" 490 2000 200 1
```

#### Teleporting a player to a coordinate with pitch/yaw

```
/TP [Target Player] [X] [Y] [Z] [Pitch] [Yaw] [Keep Velocity]
```

Teleports a player to a specified location with coordinates in the world.
Now with pitch and yaw.

!!! note

    - Pitch seems to not work.
    - Yaw only applies to your character in third person,
    where the angle of your character is changed.

| Parameter     | Type    | Description                                                                  |
| ------------- | ------- | ---------------------------------------------------------------------------- |
| Target Player | String  | Name of player to teleport                                                   |
| X             | Number  | X coordinate of the destination, in micro-units                              |
| Y             | Number  | Y coordinate of the destination, in micro-units                              |
| Z             | Number  | Z coordinate of the destination, in micro-units                              |
| Pitch         | Number  | Rotation around the Y axis in degrees                                        |
| Yaw           | Number  | Rotation around the Z axis in degrees                                        |
| Keep Velocity | Boolean | Whether or not to retain velocity after teleporting<br>1 = true<br>0 = false |

``` title='Example: Teleporting player "Cathy" to a destination, with pitch/yaw, resetting velocity'
/TP "Cathy" 1000 1250 1500 40 60 0
```

### `/Back`

Teleports you back to the last location you were teleported from.

If you add a player name to the command, this teleports the target player back to the last location they were teleported from.

| Parameter | Type   | Description                     |
| --------- | ------ | ------------------------------- |
| Player    | String | Name of player to teleport back |

``` title='Example: Teleporting player "Frisk" back to their last location'
/Back "Frisk"
```

### `/Spectator`

Toggles spectator mode, where you can freely move your camera.
This removes your character until turned off.

Highly useful for discreet moderation when you want to observe someone's behavior after reports.

This command is not usable in minigames.

### `/Spectate`

Sending only the command itself will leave spectator mode and respawn your player.

#### Spectating another player

```
/Spectate [Player]
```

If you add a player name to the command, the game turns on spectator mode and spectates the specified player.
This removes your character until turned off.

| Parameter | Type   | Description                |
| --------- | ------ | -------------------------- |
| Player    | String | Name of player to spectate |

``` title='Example: Spectating a player named "Siffrin"'
/Spectate "Siffrin"
```

This command is not usable in minigames.

## Moderation commands

### `/GrantRole`

Grants a role to a player.

| Parameter           | Type   | Description                         |
| ------------------- | ------ | ----------------------------------- |
| Role *(required)*   | String | Name of role to grant               |
| Player *(required)* | String | Name of player to grant the role to |

``` title='Granting the role "Lucid" to the player "Blocks"'
/grantrole "Lucid" "Blocks"
```

### `/RevokeRole`

Removes a role from a player.

| Parameter           | Type   | Description                       |
| ------------------- | ------ | --------------------------------- |
| Role *(required)*   | String | Name of role to revoke            |
| Player *(required)* | String | Name of player to revoke the role |

``` title='Example: Revoking the role "Depressed" player "Sunny" has'
/revokerole "Depressed" "Sunny"
```

### `/Kick`

Disconnects a player from the server.
You can also add a reason for kicking which is optional.

| Parameter           | Type   | Description            |
| ------------------- | ------ | ---------------------- |
| Player *(required)* | String | Name of player to kick |
| Reason              | String | Reason for kicking     |

``` title="Example: Kicking without reason"
/kick "Wheatley"
```

``` title="Example: Kicking with reason"
/kick "GLaDOS" "Potatoes are not allowed on the server."
```

### `/Ban`

Bans a player from the server.
You can also add a reason for banning which is optional.

| Parameter           | Type   | Description                                                             |
| ------------------- | ------ | ----------------------------------------------------------------------- |
| Player *(required)* | String | Name of player to ban                                                   |
| Time *(required)*   | Number | How many minutes to ban the player for.<br>Type -1 for a permanent ban. |
| Reason              | String | Reason for banning                                                      |

``` title="Example: Banning without reason for an hour"
/ban "lobster enjoyer" 60
```

``` title="Example: Banning with reason for a day"
/ban "lobster addict" 1440 "your lobster is too buttered"
```

``` title="Example: Banning with reason permanently"
/ban "lobster aficionado" -1 "Your butter has lobster in it"
```

### `/Unban`

Unbans the player from the server.

| Parameter           | Type   | Description             |
| ------------------- | ------ | ----------------------- |
| Player *(required)* | String | Name of player to unban |

``` title='Example: Unbanning the player "lobster hater"'
/unban "lobster hater"
```

## Player clean up commands

You can undo these operations by pressing ++lctrl+z++ if you think you have made a mistake.

### `/ClearBricks`

Clears your own bricks **and** entities.

### `/ClearEntities`

Clears your own entities.

### `/ClearLooseEntities`

Clears your entities that aren't connected to joints.

### `/ClearFarEntities`

Clears all of your entities that go beyond the specified distance relative to your location.

| Parameter             | Type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| Distance *(required)* | Number | Distance in studs to start clearing entities from |

``` title="Example: Clearing your own entities located further than 10,000 studs"
/ClearFarEntities 10000
```

## Server-wide clean up commands

You can undo these operations by pressing ++lctrl+z++ if you think you have made a mistake.

Some commands are exempt from being included in your history, so exercise caution for those commands.

### `/ClearBricks`

Clears another player's bricks **and** entities.

| Parameter           | Type   | Description                            |
| ------------------- | ------ | -------------------------------------- |
| Player *(required)* | String | Name of the bricks and entities' owner |

``` title="Example: Clearing all of Jane B. Ricks' bricks and entities"
/ClearBricks "Jane B. Ricks"
```

### `/ClearEntities`

Clears all of another player's entities.

| Parameter           | Type   | Description                 |
| ------------------- | ------ | --------------------------- |
| Player *(required)* | String | Name of the entities' owner |

``` title="Example: Clearing all of John Doe's entities"
/ClearEntities "John Doe"
```

### `/ClearLooseEntities`

Clears another player's entities that aren't connected to joints.

| Parameter           | Type   | Description                 |
| ------------------- | ------ | --------------------------- |
| Player *(required)* | String | Name of the entities' owner |

``` title="Example: Clearing Jane Doe's entities"
/ClearLooseEntities "Jane Doe"
```

### `/ClearFarEntities`

Clears all of another player's entities that go beyond the specified distance relative to your location.

| Parameter             | Type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| Player *(required)*   | String | Name of the entities' owner                       |
| Distance *(required)* | Number | Distance in studs to start clearing entities from |

``` title="Example: Clearing John B. Lock's entities located further than 5,000 studs"
/ClearFarEntities "John B. Lock" 5000
```

### `/ClearAllFarEntities`

!!! danger "Not undoable!"

Clears all entities that go beyond the specified distance relative to your location.

| Parameter             | Type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| Distance *(required)* | Number | Distance in studs to start clearing entities from |

``` title="Example: Clearing every entity located further than 10,000 studs"
/ClearAllFarEntities 10000
```

### `/ClearAllBricks`

!!! danger "Not undoable!"

Clears all bricks and all entities in the world.

### `/ClearAllEntities`

!!! danger "Not undoable!"

Clears every entity in the world, including physics objects and brick grids.

## Useless commands

### `/Ghost`

In the open alpha, this command used to be present as an actual toggle for ghosting.

> Tells you to get with the times. /ghost is a keybind now, you know.

Now it's just telling you to use the keybind.
