---
icon: lucide/book-search
tags:
    - Wires
    - Gates
    - Zones
---

# Get Entities In Zone

{{gate_availability("everyone")}}

!!! note

    This gate only works if the zone that outputs the
    {{var_display("Zone Reference","special")}} sent to the gate
    has the [Entity Detection]() option enabled, otherwise this
    gate will output nothing.

When activated with an {{var_display("Exec","exec")}} signal to the
input, this gate will overwrite the array referenced by the
{{var_display("Array Var Ref","reference","array")}} with references
of the brick grids and physics objects that were inside the zone
referenced by the {{var_display("Zone Reference","special")}} at the
time of activation.

You can filter by entity tag to only include specific brick grids
and physics objects with a specific tag in the array.

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
the referenced brick grids and physics objects with the tag in the
array.

Otherwise, if empty, the gate will include all referenced brick
grids and physics objects in the array.
