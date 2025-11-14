---
icon: material/application-variable-outline
---

# Value Types

Values have their own data types which are important to know for
gates and wiring.

## **:material-sort-bool-ascending: Boolean**{.bool}

**Also known as:** True/False

A *boolean value* is a value that represents an on/off
state. It is usually used for things that require switches.

A Boolean value consists of two states:

* :material-close: False
* :material-check: True

This can also be represented as a number
through Boolean value to Integer value/Float value conversion:

| Boolean                | Integer | Float |
| ---------------------- | ------- | ----- |
| :material-close: False | 0       | 0.00  |
| :material-check: True  | 1       | 1.00  |

Any Integer/Float value that is higher than 1 will be instantly
converted into True.

### Boolean to Exec

While you are able to use buttons with Exec as normal...

If Boolean is plugged into an Exec port straight from a switch,
it will not detect when the switch is off. Instead, put a
Edge Detector somewhere along the connection between the switch
and the Exec port of your desired gate.

This is because Exec ports will not detect a Boolean going from
True to False.

## **:material-numeric: Integer**{.int}

An *integer* is a value that represents a full or whole number
without decimal digits, can be positive or negative. For example:

* 4
* -68
* 1095
* -560

## **:material-decimal-increase: Float**{.float}

A *float* is a value that represents numerical values with
decimal digits, can be positive or negative. For example:

* 0.3
* -5.75
* 12.758
* -25.1491

## **:material-arrow-expand-right: Exec**{.exec}

"Exec" is shorthand for *Execute.*

Exec is not a data type that stores information like numbers or
strings. Instead, it serves as a trigger for many such gates that
have Exec input, or some cases even an Exec output.

Exec will detect almost any change like an Edge Detector, apart from
values that are identical to 0 or False.

It allows sequencing multiple actions on your wire circuits in
chronological order.

## **:material-cube-send: Entity**{.ent}

"Entity" in this context refers to brick grids which are referencable by
variables. Can store a parent brick grid and all its physics object that
are its children.

Anything that falls under the [Physics Object](Entities.md#physics-object)
umbrella cannot be referencable, as there is no way to attach a reference
to such objects.
