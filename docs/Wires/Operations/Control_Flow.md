---
icon: material/source-branch
tags:
    - Gates
---

# Control Flow

## Branch

When recieved a Exec pulse, trigger one of two Exec outputs
depending on a Boolean value.

=== ":material-circle-outline: False"

    If the Boolean value is **False**:

    ![Branch gate if the input is False]()
    
    The gate will trigger the lower Exec wire output
    upon a Exec pulse.

=== ":material-circle: True"

    If the Boolean value is **True**:

    ![Branch gate if the input is True]()
    
    The gate will trigger the upper Exec wire output
    upon a Exec pulse.

## Exec Union

Described in-game as a "OR" gate for Exec wires.

Merge two Exec wire paths together into one Exec wire path. Useful
if you want two or more Exec wire paths to trigger the same action(s).
