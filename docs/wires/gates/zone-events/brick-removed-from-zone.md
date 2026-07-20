---
icon: material/toy-brick-minus-outline
tags:
    - Wires
    - Gates
    - Zones
    - Building
---

# Brick Removed from Zone Event

{{gate_availability("everyone")}}

This gate sends an {{var_display("Exec","exec")}} signal when you
delete a brick inside the zone referenced by the
{{var_display("Zone Reference","special")}} input.

!!! note

    Bricks on another brick grid will not be detected.

## Ports

<div class="grid cards" markdown>

-   **Inputs:**

    - Zone Reference: {{var_display("Zone Reference","special")}}

-  **Outputs:**

    - Exec: {{var_display("Exec","exec")}}

</div>
