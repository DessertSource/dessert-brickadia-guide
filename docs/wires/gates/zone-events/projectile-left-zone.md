---
icon: lucide/square-arrow-right-exit
tags:
    - Wires
    - Gates
    - Zones
---

# Projectile Left Zone Event

{{gate_availability("everyone")}}

!!! note

    This gate only works if the zone that outputs the
    {{var_display("Zone Reference","special")}} sent to the gate
    has the [Projectile Detection]() option enabled, otherwise this
    gate will output nothing.

When a projectile leaves the zone referenced by the 
{{var_display("Zone Reference","special")}} input,
the gate will store and output the following data:

- {{var_display("Projectile","reference")}} - The reference of the
projectile that left the zone.
- {{var_display("Character","reference")}} - The reference of the
player or bot that shot this projectile.
- {{var_display("Weapon","reference")}} - The reference of the weapon
type that this projectile came from.
- {{var_display("Weapon Name","string")}} - The name of the weapon
that this projectile came from. Custom names are allowed.

An {{var_display("Exec","exec")}} signal will be sent when a
projectile leaves the zone.

## Ports

<div class="grid cards" markdown>

-   **Inputs:**

    - Zone Reference: {{var_display("Zone Reference","special")}}

-  **Outputs:**

    - Exec: {{var_display("Exec","exec")}}
    - Projectile: {{var_display(None,"reference")}}
    - Character: {{var_display(None,"reference")}}
    - Weapon: {{var_display(None,"reference")}}
    - Weapon Name: {{var_display(None,"string")}}

</div>
