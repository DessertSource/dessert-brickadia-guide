---
icon: material/math-compass
---

# Math Gates

These gates are based on real-world mathematics. You will need ample knowledge to
use these gates itself, so it is recommended you recap or read on real-world mathematics
fundamentals.

!!! note

    If you often struggle with mathematics or have
    [dyscalculia](https://en.wikipedia.org/wiki/Dyscalculia),
    these gates may not be suitable for your usage. In this case, you
    might want to ask for the help of someone else to guide you through
    these gates.

## :material-plus-thick: Add

![Add Gate](../../assets/diagrams/gates/Add_Gate.svg)

This gate outputs the sum of both inputs
($\text{Input A} + \text{Input B} = \text{Output}$).

![Using negative values on add gates](../../assets/diagrams/gates/Add_Negative.svg)

This gate will add or subtract based on **Input B**.

* If *Input B* is **positive**, the gate will do addition as normal.
<br> $A + B = \text{Output}$
* If *Input B* is **negative**, the gate will do subtraction instead.
<br> $(A + -B) \rightarrow (A - B) = \text{Output}$

These rules **do not** apply to **Input A**. *Input A* can either be positive or negative
without any effect to the functionality.

## Subtract

![Subtract Gate](../../assets/diagrams/gates/Subtract_Gate.svg)

This gate outputs the product of subtracting Input A with Input B
($\text{Input A} - \text{Input B} = \text{Output}$).

![Using negative values on subtract gates](../../assets/diagrams/gates/Subtract_Negative.svg)

This gate will subtract or add based on **Input B**.

* If *Input B* is **positive**, the gate will do subtraction as normal.
<br> $A - B = \text{Output}$
* If *Input B* is **negative**, the gate will do addition instead.
<br> $(A - -B) \rightarrow (A + B) = \text{Output}$

These rules **do not** apply to **Input A**. *Input A* can either be positive or negative
without any effect to the functionality.

## :material-close-thick: Multiply

![Multiply Gate](../../assets/diagrams/gates/Multiply_Gate.svg)

This gate outputs the product of multiplying both inputs
($\text{Input A} \times \text{Input B} = \text{Output}$).

![Using negative values on multiplication gates](../../assets/diagrams/gates/Multiply_Negative.svg)

* If the inputs are both positive or negative, the output always
comes out as **positive**.
* If either individual input has a negative value and the other
has a positive value, the output always comes out as **negative**.

### :material-fraction-one-half: Using Multiply for division

You can insert float values containing decimals to multiply with
other values, which may prove useful in scenarios where using *Multiply*
gates over *Divide* gates are preferred.

![Dividing 10 by 2 with multiply gates.](../../assets/diagrams/gates/Multiply_Division.svg)

### :material-exponent: Using Multiply for exponents

For the power of 2, you need to connect the same wire containing the
value to both inputs of the *Multiply* gate.

Shown in this example is $4^2$, alternatively read as *4 to the power of 2*.

![A circuit showing 4 being raised by the power of 2.](../../assets/diagrams/gates/Multiply_Exponents_1.svg)

You will need to chain 2 *Multiply* gates or more to handle operations
involving exponents that are above 2.

This example achieves $8^2$, $8^3$ and $8^4$, all in one circuit.

![A circuit showing 8 being raised by the power of 2, 3 and 4.](../../assets/diagrams/gates/Multiply_Exponents_2.svg)

## :material-division: Divide

![Divide Gate](../../assets/diagrams/gates/Divide_Gate.svg)

This gate outputs the product of dividing both inputs
($\text{Input A} \div \text{Input B} = \text{Output}$).
Division can also be represented by using fractions.

![Using negative values on divide gates](../../assets/diagrams/gates/Divide_Negative.svg)

* If the inputs are both positive or negative, the output always
comes out as **positive**.
* If either individual input has a negative value and the other
has a positive value, the output always comes out as **negative**.

### :material-decimal: Using Divide for multiplication

You can insert float values containing decimals to divide with
other values, which may prove useful in scenarios where using *Divide*
gates over *Multiply* gates are preferred.

![Multiplying 2 by 4 with divide gates.](../../assets/diagrams/gates/Divide_Multiplication.svg)

## :material-chart-bell-curve-cumulative: Blend

This gate is based on linear interpolation (alternatively called a Lerp).

The linear interpolation formula:

$$y = y_{0} + (x-x_{0})\frac{y_{1}-y_{0}}{x_{1}-x_{0}}$$

## :material-percent: Modulo

## :material-percent: Modulo Floor

Python modulo