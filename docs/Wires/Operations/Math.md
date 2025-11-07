---
icon: material/math-compass
tags:
    - Gates
---

# Math

These gates are based on real-world mathematics. You will need ample knowledge to
use these gates itself, so it is recommended you recap or read on real-world mathematics
fundamentals.

## :material-plus-thick: Add

![Add Gate](../../assets/diagrams/wires/gates/math/Add_Gate.svg)

This gate outputs the sum of both inputs
($\text{Input A} + \text{Input B} = \text{Output}$).

![Using negative values on add gates](../../assets/diagrams/wires/gates/math/Add_Negative.svg)

This gate will add or subtract based on **Input B**.

* If *Input B* is **positive**, the gate will do addition as normal.
<br> $A + B = \text{Output}$
* If *Input B* is **negative**, the gate will do subtraction instead.
<br> $(A + -B) \rightarrow (A - B) = \text{Output}$

These rules **do not** apply to **Input A**. *Input A* can either be positive or negative
without any effect to the functionality.

## :material-minus-thick: Subtract

![Subtract Gate](../../assets/diagrams/wires/gates/math/Subtract_Gate.svg)

This gate outputs the product of subtracting Input A with Input B
($\text{Input A} - \text{Input B} = \text{Output}$).

![Using negative values on subtract gates](../../assets/diagrams/wires/gates/math/Subtract_Negative.svg)

This gate will subtract or add based on **Input B**.

* If *Input B* is **positive**, the gate will do subtraction as normal.
<br> $A - B = \text{Output}$
* If *Input B* is **negative**, the gate will do addition instead.
<br> $(A - -B) \rightarrow (A + B) = \text{Output}$

These rules **do not** apply to **Input A**. *Input A* can either be positive or negative
without any effect to the functionality.

## :material-close-thick: Multiply

![Multiply Gate](../../assets/diagrams/wires/gates/math/Multiply_Gate.svg)

This gate outputs the product of multiplying both inputs
($\text{Input A} \times \text{Input B} = \text{Output}$).

![Using negative values on multiplication gates](../../assets/diagrams/wires/gates/math/Multiply_Negative.svg)

* If the inputs are both positive or negative, the output always
comes out as **positive**.
* If either individual input has a negative value and the other
has a positive value, the output always comes out as **negative**.

### :material-fraction-one-half: Using Multiply for division

You can insert float values containing decimals to multiply with
other values, which may prove useful in scenarios where using *Multiply*
gates over *Divide* gates are preferred.

![Dividing 10 by 2 with multiply gates.](../../assets/diagrams/wires/gates/math/Multiply_Division.svg)

### :material-exponent: Using Multiply for exponents

For the power of 2, you need to connect the same wire containing the
value to both inputs of the *Multiply* gate.

Shown in this example is $4^2$, alternatively read as *4 to the power of 2*.

![A circuit showing 4 being raised by the power of 2.](../../assets/diagrams/wires/gates/math/Multiply_Exponents_1.svg)

You will need to chain 2 *Multiply* gates or more to handle operations
involving exponents that are above 2.

This example achieves $8^2$, $8^3$ and $8^4$, all in one circuit.

![A circuit showing 8 being raised by the power of 2, 3 and 4.](../../assets/diagrams/wires/gates/math/Multiply_Exponents_2.svg)

## :material-division: Divide

![Divide Gate](../../assets/diagrams/wires/gates/math/Divide_Gate.svg)

This gate outputs the product of dividing both inputs
($\text{Input A} \div \text{Input B} = \text{Output}$).
Division can also be represented by using fractions.

![Using negative values on divide gates](../../assets/diagrams/wires/gates/math/Divide_Negative.svg)

* If the inputs are both positive or negative, the output always
comes out as **positive**.
* If either individual input has a negative value and the other
has a positive value, the output always comes out as **negative**.

### :material-decimal: Using Divide for multiplication

You can insert float values containing decimals to divide with
other values, which may prove useful in scenarios where using *Divide*
gates over *Multiply* gates are preferred.

![Multiplying 2 by 4 with divide gates.](../../assets/diagrams/wires/gates/math/Divide_Multiplication.svg)

## :material-chart-bell-curve-cumulative: Blend

![Blend Gate](../../assets/diagrams/wires/gates/math/Blend_Gate.svg)

To simplify this down with a brief explanation: this gate is commonly
used to:

* Select a set of numbers based on an
[:material-decimal-increase: Float value](){.float}.
* Output two numbers depending on a
[:material-sort-bool-ascending: Boolean value](){.bool}.

This gate is based on linear interpolation
(alternatively called a Lerp in computer terms).

### Formula

We will show the linear interpolation formula:

$$y = y_{0} + (x-x_{0})\frac{y_{1}-y_{0}}{x_{1}-x_{0}}$$

This gate uses the same formula, but swaps out the variables
for the inputs' values:

$$\text{Output} = \text{Input A} + (\text{Blend Value}-0)\frac{\text{Input B}-{\text{Input A}}}{1-0}$$

To cut down on redundancy, we will simplify the formula down to this:

$$\text{Output} = \text{A} + (\text{Blend Value})(\text{B}-{\text{A}})$$

### Examples

=== "Boolean value as blend value"

    A Boolean value can only either be 0 (false) or 1 (true),
    which makes it a perfect candidate if you just want to use
    the Blend gate to make a switch output between two custom
    values.

    Given *Input A* is **10** and *Input B* is **20**.
    If *Blend Value* is...:

    === ":material-circle-outline: False"

        ![Example of blend gate with a False boolean value](../../assets/diagrams/wires/gates/math/Blend_Bool_False.svg)

        The Blend gate outputs **10**.

    === ":material-circle: True"

        ![Example of blend gate with a True boolean value](../../assets/diagrams/wires/gates/math/Blend_Bool_True.svg)

        The Blend gate outputs **20**.

=== "Float value as blend value"

    Since this warrants the use of the equation above,
    we will use it to demonstrate how the Blend Gate outputs
    a value.

    ![Example of blend gate with its output hidden](../../assets/diagrams/wires/gates/math/Blend_Float_Unrevealed.svg)

    Given input A is **50** and input B is **80**, and
    the blend value is **0.37**:

    First, we subtract 80 ($\text{B}$)
    by 50 ($\text{A}$). 30 is the result.

    $$\text{Output} = 50 + (0.37)(80-50)$$

    Multiply the blend value with the result of
    $(\text{B}-\text{A})$. The result is 11.1.

    $$\text{Output} = 50 + (0.37)(30)$$

    Finally, get the sum of Input A and the result of
    $(\text{Blend Value})(\text{B}-\text{A})$.

    $$\text{Output} = 50 + 11.1$$

    You have the gate's final output.

    $$\text{Output} = 61.1$$

    ![Example of blend gate with a float blend value](../../assets/diagrams/wires/gates/math/Blend_Float_Result.svg)

## Ceil

![Ceil Gate](../../assets/diagrams/wires/gates/math/Ceil_Gate.svg)

This gate rounds an float value up to the higher integer equivalent.

Two examples of Ceil:

* If the input is **5.06**, it is rounded up to the integer of **6**.<br>
![5.06 being rounded up using a Ceil gate](../../assets/diagrams/wires/gates/math/Ceil_Example_1.svg)
* If the input is **8.83**, it is rounded up to the integer of **9**.<br>
![8.83 being rounded up using a Ceil gate](../../assets/diagrams/wires/gates/math/Ceil_Example_2.svg)

## Floor

![Floor Gate](../../assets/diagrams/wires/gates/math/Floor_Gate.svg)

This gate rounds an float value down to the lower integer equivalent.

Two examples of Floor:

* If the input is **2.46**, it is rounded down to the integer of **2**.<br>
![2.46 being rounded down using a Floor gate](../../assets/diagrams/wires/gates/math/Floor_Example_1.svg)
* If the input is **3.71**, it is rounded down to the integer of **3**.<br>
![3.71 being rounded down using a Floor gate](../../assets/diagrams/wires/gates/math/Floor_Example_2.svg)

## :material-percent: Modulo

![Modulo Gate](../../assets/diagrams/wires/gates/math/Modulo_Gate.svg)

This gate extracts the remainder of a division equation.

If your numbers are evenly subtractable, this gate will output
zero. For example:

* $12 \div 4 = 3$, leaving no remainder.<br>
![Modulo Example 1](../../assets/diagrams/wires/gates/math/Modulo_Example_1.svg)
* $600 \div 10 = 60$ leaving no remainder.<br>
![Modulo Example 2](../../assets/diagrams/wires/gates/math/Modulo_Example_2.svg)

On the other hand, here's some
examples of division that output non-zero values with Modulo:

* $24 \div 7 = 4$ with a remainder of $3$.<br>
![Modulo Example 3](../../assets/diagrams/wires/gates/math/Modulo_Example_3.svg)
* $95 \div 15 = 6$ with a remainder of $5$.<br>
![Modulo Example 4](../../assets/diagrams/wires/gates/math/Modulo_Example_4.svg)

### Modulo (Floor)

![Modulo Floor Gate](../../assets/diagrams/wires/gates/math/Modulo_Floor_Gate.svg)

Does the same as the Modulo gate but rounds the value down
to an equivalent lower integer.

* $17.6 \div 5 = 3$ with a remainder of $2.6$,
floored down to $2$.<br>
![Modulo with Floor](../../assets/diagrams/wires/gates/math/Modulo_Floor_Example.svg)
