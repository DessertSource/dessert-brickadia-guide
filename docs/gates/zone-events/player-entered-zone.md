---
icon: material/account-box-plus-outline
tags:
    - Wires
    - Gates
    - Zones
    - Entity tags
    - Collision channels
---

# Player Entered Zone Event

{{gate_availability("everyone")}}

When a player or a bot enters the zone referenced by the 
{{var_display("Zone Reference","special")}} input, the gate will
output an {{var_display("Exec","exec")}} signal and a reference of
the player or bot that entered the zone last through the
{{var_display("Player","reference")}} output.

You can filter by entity tag to only activate the gate when the
player or bot has a specific tag.

## Ports

<div class="grid cards" markdown>

-   **Inputs:**

    - Zone Reference: {{var_display("Zone Reference","special")}}
    - Tag Filter: {{var_display(None,"string")}}

-  **Outputs:**

    - Exec: {{var_display("Exec","exec")}}
    - Player: {{var_display(None,"reference")}}

</div>

## Hidden ports

<div class="grid cards" markdown>

- [**Collision settings:**](#collision-settings)
    - Player 1 Detection: {{var_display(None,"boolean")}}
    - Player 2 Detection: {{var_display(None,"boolean")}}
    - Player 3 Detection: {{var_display(None,"boolean")}}
    - Player 4 Detection: {{var_display(None,"boolean")}}

</div>

## Filter settings

### Tag filter {{var_display("","string")}}

If this is set to an existing tag, the gate only sends an Exec
signal and a player reference when the player or bot has that
specific tag. Only one tag is allowed.

Otherwise, if empty, the gate will send an Exec signal and a player
reference for every player or bot that enters the zone.

## Collision settings

### Player 1 Detection {{var_display("","boolean")}}

Whether to send an Exec signal and a player reference when players
and bots in collision channel 1 enter the zone.

### Player 2 Detection {{var_display("","boolean")}}

Whether to send an Exec signal and a player reference when players
and bots in collision channel 2 enter the zone.

### Player 3 Detection {{var_display("","boolean")}}

Whether to send an Exec signal and a player reference when players
and bots in collision channel 3 enter the zone.

### Player 4 Detection {{var_display("","boolean")}}

Whether to send an Exec signal and a player reference when players
and bots in collision channel 4 enter the zone.
