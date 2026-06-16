---
icon: lucide/waypoints
tags:
    - Wires
---

# Execution signals

!!! note

    The game uses the term "Exec", but for the sake of simplicity, we will use the full word "Execution".

Execution signals can be used to trigger Execution-based gates and allow you to organize the order of those gates.

Execution-based gates output another execution signal once they're done running after they recieve an execution signal input.

All of this makes it possible to create a daisy chain of gates in a sequence:

``` mermaid
graph LR

A["Gate A"]
B["Gate B"]
C["Gate C"]

A -- "Exec" --> B
B -- "Exec" --> C
```

| Tick # | Gate           |
| ------ | -------------- |
| 1      | Gate A         |
| 2      | Gate B         |
| 3      | Gate C         |

## How execution signals work

Value changes will trigger an outgoing execution signal that lasts one tick,
provided the value being changed to must not be 0 in numerical form.
This means that the following values for their respective data type:

- {{var_display(False,"boolean")}}
- {{var_display(0,"integer")}}
- {{var_display(0.00,"float")}}

...will not trigger an outgoing execution signal.

Execution signals have a data type dedicated to them: {{var_display(None,"exec")}}
