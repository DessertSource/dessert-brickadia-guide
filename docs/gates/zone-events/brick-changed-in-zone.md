---
icon: material/toy-brick-plus-outline
tags:
    - Wires
    - Gates
    - Zones
    - Building
---

# Brick Changed in Zone Event

{{gate_availability("everyone")}}

This gate sends an {{var_display("Exec","exec")}} signal when you
do one of the following building actions inside the zone referenced
by the {{var_display("Zone Reference","special")}} input:

- Placing a brick
- Painting a birkc or fill painting bricks
- Resizing, rotating, reorienting or moving a brick
- Changing a brick's properties
- Adding or deleting a brick's components (editing does not apply)

!!! note

    Bricks on another brick grid will not be detected.

## Ports

<div class="grid cards" markdown>

-   **Inputs:**

    - Zone Reference: {{var_display("Zone Reference","special")}}

-  **Outputs:**

    - Exec: {{var_display("Exec","exec")}}

</div>
