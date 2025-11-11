---
icon: material/cube-send
---

# Entities

An entity refers to the physical objects that are not part of the
global brick grid. This is designed that way so certain things can
move around or be transformed around the world while some of the things
you build can stay static and not incur a performance cost.

## **Character**{.glo}

A character refers to either a player or bot, as both of these
share the same base mechanics of being able to move and use items.

There are distinct differences and shared similarities between them.

* Bots are permanent 24/7. Players are not.
* Bots have their own behavior and act like players,
but are not players.
* You can apply all wire-induced effects to both bots
and players.
* Both bots and players can use avatars.

### Which types of character should I focus on?

It is important to take into account the type of mechanics you
are going to implement in your World, therefore here is an easy
table for game designers:

| Game Type                           | Players          | Bots             |
| ----------------------------------- | ---------------- | ---------------- |
| PvP (Player vs Player)              | :material-check: | :material-close: |
| PvE (Player vs Enemies)             | :material-close: | :material-check: |
| PvPvE (Player vs Player vs Enemies) | :material-check: | :material-check: |

## **Brick Grid**{.glo}

A type of entity that can store the following:

* Bricks
* Components
* Wires
* Other brick grids
* Non-brick grid physics objects
(when attached to joints in grid)

## **Physics Object**{.glo}

Physics objects like wheels and the ball that fall under
non-Brick Grid entities. They cannot be wired to,
but can be attached to brick grids and their respective joints.
