---
icon: material/cube-unfolded
tags:
    - Gates
---

# Bitwise

!!! warning "Advanced concepts ahead!"

    These gates are mostly used for complex contraptions.
    They are not *essential* to understanding wires. It is a
    common occurence that people struggle upon reading about
    the concepts of bits.

Bitwise gates are a set of gates based on [Logic](./Logic.md) gates
but also have their own shift left/right modifier gates.

The difference is that while those interpret values as numbers,
these ones interpret the values as a bit representation of them.
From there, the gates do a conditional check for each digit of
the input values given as a bit representation.

All inputs in these gates that are
[:material-decimal-increase: Float values](){.float}
get converted into
[:material-numeric: Integer values](){.int}.
This means that float values are not recommended for bitwise gates
and you should avoid using them to plug into bitwise gates as much
as possible.

## About bits

Numbers can be represented in bits, which represent either
0 or 1 in each digit, meaning they are binary.
Bits make up the sum of the number they represent.
They are the most basic data form in computing.

All digits that represent bits can be translated to powers of 2.
If we pick the sixth digit as an example, it should come out
as 2^5^ which is equivalent to 32. It is as easy as this:

$$n^\text{th} \text{ digit} = 2^{n-1}$$

### Example number

For example, if we have 38, the bit representation is:

$$100110$$

Before we translate these bits, we reverse them *visually*
to get a better picture before going into the equation.

$$011001$$

This means that we can translate these bits into the following
equation:

$$38 = 0(2^0) + 1(2^1) + 1(2^2) + 0(2^3) + 0(2^4) + 1(2^5)$$

Convert all numbers with exponents.
(*Mathematical note: 2^0^ = 1*)

$$38 = 0(1) + 1(2) + 1(4) + 0(8) + 0(16) + 1(32)$$

Gotta Multiply 'Em All and get:

$$38 = 0 + 2 + 4 + 0 + 0 + 32$$

Simplify the equation above to this:

$$38 = 2 + 4 + 32$$

The final result:

$$38 = 38$$

## :material-tilde: NOT (Bitwise)

![NOT (Bitwise) Gate](../../assets/diagrams/wires/operations/bitwise/NOT_Bitwise.svg)

## :material-ampersand: AND (Bitwise)

![AND (Bitwise) Gate](../../assets/diagrams/wires/operations/bitwise/AND_Bitwise.svg)

## :material-drag-vertical-variant: OR (Bitwise)

![OR (Bitwise) Gate](../../assets/diagrams/wires/operations/bitwise/OR_Bitwise.svg)

## :material-chevron-up: XOR (Bitwise)

![XOR (Bitwise) Gate](../../assets/diagrams/wires/operations/bitwise/XOR_Bitwise.svg)

## :material-ampersand: NAND (Bitwise)

![NAND (Bitwise) Gate](../../assets/diagrams/wires/operations/bitwise/NAND_Bitwise.svg)

## :material-drag-vertical-variant: NOR (Bitwise)

![NOR (Bitwise) Gate](../../assets/diagrams/wires/operations/bitwise/NOR_Bitwise.svg)

## :material-chevron-left-box-outline: Shift Left

![Shift Left Gate](../../assets/diagrams/wires/operations/bitwise/Shift_Left.svg)

## :material-chevron-right-box-outline: Shift Right

![Shift Right Gate](../../assets/diagrams/wires/operations/bitwise/Shift_Right.svg)
