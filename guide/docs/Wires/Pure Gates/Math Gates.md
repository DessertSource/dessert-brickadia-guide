---
icon: material/math-compass
---

# Math Gates

These gates cover the four basic operations of mathematics.

## Add

Add the value of **Input B** to **Input A**.

$$ a + b = \text{output} $$

## Subtract

Subtracts the value of **Input A** with the value of **Input B**.
Order sensitive.

$$ a - b = \text{output}$$

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

!!! note

    Pay attention when connecting each input. Division is a
    order-sensitive operation.

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
