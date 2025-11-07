---
icon: material/gate-xnor
tags:
    - Gates
---

# Logic

These gates are based on real life logic gate principles and
all its variants. This means what you see is what you get, just
like if you were to use actual logic gates.

## :material-gate-not: NOT

![NOT Gate](../../assets/diagrams/wires/gates/logic/NOT_Gate.svg)

Depending on the following inputs:

=== ":material-circle-outline: False"

    If the input is **False**:

    ![NOT gate if the input is False](../../assets/diagrams/wires/gates/logic/NOT_False.svg)
    
    The gate will output **True**.

=== ":material-circle: True"

    If the input is **True**:

    ![NOT gate if the input is True](../../assets/diagrams/wires/gates/logic/NOT_True.svg)
    
    The gate will output **False**.

## :material-gate-and: AND

![AND Gate](../../assets/diagrams/wires/gates/logic/AND_Gate.svg)

Depending on the following inputs:

=== ":material-circle-outline: False / False"

    If both inputs are **False**:

    ![AND gate if both inputs are False](../../assets/diagrams/wires/gates/logic/AND_1.svg)
    
    The gate will output **False**.

=== ":material-circle-half-full: True / False"

    If one input is **True** and another is **False**:

    ![AND gate if one input is True and another is False](../../assets/diagrams/wires/gates/logic/AND_2.svg)
    
    The gate will output **False**.

=== ":material-circle: True / True"

    If both inputs are **True**:

    ![AND gate if both inputs are True](../../assets/diagrams/wires/gates/logic/AND_3.svg)

    The gate will output **True**.

## :material-gate-or: OR

![OR Gate](../../assets/diagrams/wires/gates/logic/OR_Gate.svg)

Depending on the following inputs:

=== ":material-circle-outline: False / False"

    If both inputs are **False**:

    ![OR gate if both inputs are False](../../assets/diagrams/wires/gates/logic/OR_1.svg)
    
    The gate will output **False**.

=== ":material-circle-half-full: True / False"

    If one input is **True** and another is **False**:

    ![OR gate if one input is True and another is False](../../assets/diagrams/wires/gates/logic/OR_2.svg)
    
    The gate will output **True**.

=== ":material-circle: True / True"

    If both inputs are **True**:

    ![OR gate if both inputs are True](../../assets/diagrams/wires/gates/logic/OR_3.svg)
    
    The gate will output **True**.

## :material-gate-xor: XOR

![XOR Gate](../../assets/diagrams/wires/gates/logic/XOR_Gate.svg)

Depending on the following inputs:

=== ":material-circle-outline: False / False"

    If both inputs are **False**:

    ![XOR gate if both inputs are False](../../assets/diagrams/wires/gates/logic/XOR_1.svg)
    
    The gate will output **False**.

=== ":material-circle-half-full: True / False"

    If one input is **True** and another is **False**:

    ![XOR gate if one input is True and another is False](../../assets/diagrams/wires/gates/logic/XOR_2.svg)
    
    The gate will output **True**.

=== ":material-circle: True / True"

    If both inputs are **True**:

    ![XOR gate if both inputs are True](../../assets/diagrams/wires/gates/logic/XOR_3.svg)
    
    The gate will output **False**.

## :material-gate-nand: NAND

![NAND Gate](../../assets/diagrams/wires/gates/logic/NAND_Gate.svg)

Depending on the following inputs:

=== ":material-circle-outline: False / False"

    If both inputs are **False**:

    ![NAND gate if both inputs are False](../../assets/diagrams/wires/gates/logic/NAND_1.svg)
    
    The gate will output **True**.

=== ":material-circle-half-full: True / False"

    If one input is **True** and another is **False**:

    ![NAND gate if one input is True and another is False](../../assets/diagrams/wires/gates/logic/NAND_2.svg)
    
    The gate will output **True**.

=== ":material-circle: True / True"

    If both inputs are **True**:

    ![NAND gate if both inputs are True](../../assets/diagrams/wires/gates/logic/NAND_3.svg)

    The gate will output **False**.

## :material-gate-nor: NOR

![NOR Gate](../../assets/diagrams/wires/gates/logic/NOR_Gate.svg)

Depending on the following inputs:

=== ":material-circle-outline: False / False"

    If both inputs are **False**:

    ![NOR gate if both inputs are False](../../assets/diagrams/wires/gates/logic/NOR_1.svg)
    
    The gate will output **True**.

=== ":material-circle-half-full: True / False"

    If one input is **True** and another is **False**:

    ![NOR gate if one input is True and another is False](../../assets/diagrams/wires/gates/logic/NOR_2.svg)
    
    The gate will output **False**.

=== ":material-circle: True / True"

    If both inputs are **True**:

    ![NOR gate if both inputs are True](../../assets/diagrams/wires/gates/logic/NOR_3.svg)
    
    The gate will output **False**.

## :material-chart-bell-curve: Edge Detector

![Edge Detector Gate](../../assets/diagrams/wires/gates/logic/Edge_Detector.svg)

This gate sends a one-tick pulse of **True**
whenever one of these two conditions are met:

=== ":material-arrow-up-bold: Value Increase"

    Outputs to the *Rising Edge* port when the input value **increases**.

    ![Edge Detector Gate when there's a increase in the input value](../../assets/diagrams/wires/gates/logic/Edge_Detector_Increase.svg)

=== ":material-arrow-down-bold: Value Decrease"

    Outputs to the *Falling Edge* port when the input value **decreases**.

    ![Edge Detector Gate when there's a decrease in the input value](../../assets/diagrams/wires/gates/logic/Edge_Detector_Decrease.svg)

Otherwise, this will do nothing if the input value stays static.

Best used with the input of a
[:material-sort-bool-ascending: Boolean value](){.bool}.
