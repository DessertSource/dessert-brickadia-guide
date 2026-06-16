---
icon: lucide/gamepad-directional
tags:
    - Essentials
    - Movement
---

# Movement

For beginners, movement is the one of the most important ways to interact with worlds in Brickadia.
Everything below is what you need to know about navigating the world around you.

## Walking

![Siffrin avatar walking](../assets/media/essentials/movement/walking.jpg)

The WASD control scheme is used for walking on keyboard.

- Press ++w++ to go forward.
- Press ++s++ to go backward.
- Press ++a++ to go left.
- Press ++d++ to go right.

The movement is smooth on stairs because the player has a capsule collider, which means the top and bottom of the cylinder is round.

### Slower walking

To lower your walkspeed, hold ++c++ while you are walking.
This makes your walking sounds quieter but still audible.

## Jumping

![Melanie from Regretevator avatar in the air after jumping](../assets/media/essentials/movement/jumping.jpg)

To jump, press ++space++.

Jumping allows you to get up places that aren't too high.

Jumping also allows you to cross from a place to another if the gap is small enough to jump across.

## Crouching / Ducking

![Clover avatar crouching behind a truck](../assets/media/essentials/movement/crouching.jpg)

To crouch under objects, hold ++lshift++ while you are walking.

Crouching "shrinks" your character down, giving them the ability to move under smaller gaps provided they are not lower than 9 plates.

This also silences the walking sounds at the cost of your walk speed being reduced.

## Sprinting

![Hornet avatar sprinting](../assets/media/essentials/movement/sprinting.jpg)

First, be aware that the "Tap To Sprint" setting is on by default.
If you prefer holding the key to sprint, you can change this setting.

To disable the "Tap To Sprint" setting:

1. Open the **:material-cog:{.button .item .blue} options**{.button .large} menu in the main menu or the pause menu.
2. Navigate to the **:material-square-circle:{.button .item .gray} controls**{.button .large} menu.
3. Look for the "Control Settings" header. Find the "Tap To Sprint" option under the same header.

=== "Tap To Sprint on"

    To sprint and gain walk speed, tap ++lctrl++ only once to keep sprinting until you stop moving.
    
    After you stop moving, you will be required to tap ++lctrl++ if you want to sprint again.

=== "Tap To Sprint off"

    To sprint and gain walk speed, hold ++lctrl++ while you are walking.

Sprinting is very beneficial when you demand that extra speed for better jumping.

The drawback is that sprinting makes your walking sounds louder.

## Flying

![G-man avatar flying in the air](../assets/media/essentials/movement/flying.jpg)

!!! note

    May be disabled on worlds and servers where flying and by extension, ghosting, gives you an unfair advantage.

To fly around the world, press ++v++.

You will no longer fall down and can reach practically any place you want.
Physical limitations and obstacles still apply.

Holding ++lctrl++, the run key, makes you even faster.

### Ghosting

Hold ++lalt++ and press ++v++ to toggle ghosting.

Ghosting gives you the freedom to bypass any physical limitations you would still have if you only turned on flying.
For example, you can now pass buildings made of bricks without colliding with them.

This functionality is similar to noclipping, a popular term for this kind of mode in games.

Enabling ghosting will enable flying if it is not active to avoid accidental falls into the void. Conversely, disabling flying will also disable ghosting if it is active.
