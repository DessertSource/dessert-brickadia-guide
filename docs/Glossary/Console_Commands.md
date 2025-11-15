---
icon: material/console
---

# Console Commands

This page refers to some custom console ( ++"~"++ or ++"F6"++ ) commands
that aren't default to Unreal Engine but rather, they are a byproduct
of Brickadia's features. Default Unreal Engine may be also included as fit,
due to some of them being very useful in user context.

Not all commands are included, as some aren't really useful in a user context.

Just like chat commands, you can enter an argument in quotes ("") for anything
involving spaces.

## Performance Monitoring

### `stat FPS`

Display frames per second and time per frame.

### `stat UNIT`

Display detailed breakdown of the frametime, memory, draw count and primitive
count.

Useful for diagnosing if your CPU or GPU is the issue.

### `stat UnitGraph`

Shows a visual graph if you have `stat UNIT` enabled.

## Visualization

### `Bricks.DrawDebugColliders`

Visualizes the colliders of brick grids.
Useful for debugging the simplified colliders of an object
and exclude the right bricks from being included in the calucation
of those colliders.

**Values:**

* 0: Disabled (false)
* 1: Enabled (true)

## Export

### `Bricks.Export`

Export bricks on the global grid as a .gltf file.

!!! Note

    This will not export entities or physics objects.

**Arguments:**

* **File name:** The .gltf will be named with the specified name.
It is highly recommended to close this in quotes.

**Usage example:**

```
Bricks.Export "exported gltf model name"
```
