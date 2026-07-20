---
icon: lucide/user-search
tags:
    - Wires
    - Gates
    - Zones
---

# Get Players In Zone

{{gate_availability("everyone")}}

When activated with an {{var_display("Exec","exec")}} signal to the
input, this gate will overwrite the array referenced by the
{{var_display("Array Var Ref","reference","array")}} with references
of the players and bots that were inside the zone referenced by the
{{var_display("Zone Reference","special")}} at the time of 
activation.

You can filter by entity tag to only include specific players and
bots with a specific tag in the array.

## Ports

<div class="grid cards" markdown>

-   **Inputs:**

    - Exec: {{var_display("Exec","exec")}}
    - Zone Reference: {{var_display("Zone Reference","special")}}
    - Array Var Ref: {{var_display("Reference Array","reference","array")}}
    - Tag Filter: {{var_display(None,"string")}}

-  **Outputs:**

    - Exec Out: {{var_display("Exec","exec")}}

</div>

## Filter settings

### Tag filter {{var_display("","string")}}

If this is set to an existing tag, the gate will only include 
the referenced players and bots with the tag in the array.

Otherwise, if empty, the gate will include all referenced players
and bots in the array.
