---
icon: lucide/paint-bucket
tags:
    - wires
---

# Wire colors

There are various wire colors in Brickadia which signify data types.
If applicable, the color will also appear darker or lighter depending on the value of the output being carried.

Unconnected wires have a gray color.

{{ wire_display(12, None, None) }}

Wires glow in the dark, which allows them to be visible in every environment.

## Wire arrows

Wires will show arrows pointing towards their inputs when you equip the Connector. These arrows are not visible in normal play or when equipping other tools.

## :lucide-power: Boolean

- If the Boolean is {{var_display(False,"boolean")}}, the wire will be colored dark red.
- If the Boolean is {{var_display(True,"boolean")}}, the wire will be colored red.

| Value                            | Wire Color                                            |
| -------------------------------- | ----------------------------------------------------- |
| {{var_display(False,"boolean")}} | {{ wire_display(6, "boolean", "false") }}<br>Dark red |
| {{var_display(True,"boolean")}}  | {{ wire_display(6, "boolean", "true") }}<br>Red       |

## :lucide-arrow-up-1-0: Integer

- If the integer is equal to or lower than {{var_display("0","integer")}}, the wire will be colored with a dark bluish green.
- If the integer is equal to {{var_display("1","integer")}}, the wire will be colored with a bluish green.
- If the integer is equal to or higher than {{var_display("2","integer")}}, the wire will be colored with a bright bluish green.

| Value                          | Wire Color                                                     |
| ------------------------------ | -------------------------------------------------------------- |
| {{var_display("0","integer")}} | {{ wire_display(6, "integer", "zero") }}<br>Dark bluish green  |
| {{var_display("1","integer")}} | {{ wire_display(6, "integer", "one") }}<br>Bluish green        |
| {{var_display("2","integer")}} | {{ wire_display(6, "integer", "two") }}<br>Bright bluish green |

## :lucide-decimals-arrow-right: Float

The brightness of the green color is determined from a range of 0 to 1 for the float value being carried.

- Float wires carrying negative values below {{var_display("0.00","float")}} will not turn dimmer.
- Float wires carrying values higher than {{var_display("1.00","float")}} will not turn brighter.

| Value                           | Wire Color                                            |
| ------------------------------- | ----------------------------------------------------- |
| {{var_display("0.00","float")}} | {{ wire_display(6, "float", "zero") }}<br>Dark green  |
| {{var_display("0.50","float")}} | {{ wire_display(6, "float", "half") }}<br>Green       |
| {{var_display("1.00","float")}} | {{ wire_display(6, "float", "one") }}<br>Bright green |

## :lucide-package: Entity

Entity wires have a cyan-blue color.

{{ wire_display(12, "entity", None) }}

## :lucide-split: Exec

Exec wires are usually dark gray.

When an Exec output is triggered, all outgoing wires carrying the Exec output will flash light gray for one tick.

| Value                         | Wire Color                                        |
| ----------------------------- | ------------------------------------------------- |
| {{var_display("Off","exec")}} | {{ wire_display(6, "exec", "off") }}<br>Dark gray |
| {{var_display("On","exec")}}  | {{ wire_display(6, "exec", "on") }}<br>Light gray |

## Other colors

Wire colors that are used in-game that are not colored by a specific criteria and do not correspond to a specific type.

### Blue

This is a color often used for non-standard data types.

{{ wire_display(12, "blue", None) }}
