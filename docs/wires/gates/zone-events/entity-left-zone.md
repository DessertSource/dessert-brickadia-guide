---
icon: material/text-box-remove-outline
tags:
    - Wires
    - Gates
    - Zones
    - Entity tags
---

# Entity Left Zone Event

{{gate_availability("everyone")}}

!!! note

    This gate only works if the zone that outputs the
    {{var_display("Zone Reference","special")}} sent to the gate
    has the [Entity Detection]() option enabled, otherwise this
    gate will output nothing.

When a brick grid or physics object leaves the zone referenced by
the {{var_display("Zone Reference","special")}} input,
the gate will output an {{var_display("Exec","exec")}} signal and a
reference of the brick grid or physics object that left the zone
last through the {{var_display("Entity","reference")}} output.

You can filter by entity tag to only activate the gate when the
brick grid or physics object has a specific tag.

## Ports

<div class="grid cards" markdown>

-   **Inputs:**

    - Zone Reference: {{var_display("Zone Reference","special")}}
    - Tag Filter: {{var_display(None,"string")}}

-  **Outputs:**

    - Exec: {{var_display("Exec","exec")}}
    - Entity: {{var_display(None,"reference")}}

</div>

## Filter settings

### Tag filter {{var_display("","string")}}

If this is set to an existing tag, the gate only sends an Exec
signal and an entity reference when the brick grid or physics object
has that specific tag. Only one tag is allowed.

Otherwise, if empty, the gate will send an Exec signal and an entity
reference for every brick grid or physics object that leaves the
zone.
