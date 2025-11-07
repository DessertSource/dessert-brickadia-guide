---
icon: material/toy-brick-search-outline
tags:
    - Gates
---

# Brick Grids

Gates that involve the functionality of entities considered as physics grids.

## Read Brick Grid

![Read Brick Grid Gate](../../assets/diagrams/wires/gates/entities/Read_Brick_Grid_Gate.svg)

This gate turns physics grids into referenceable entities for use on other gates.

![Physics grids](../../assets/pictures/wires/gates/entities/Read_Brick_Grid_on_grids.svg)

Only one of this gate is needed per physics grid,
since the only function this does is provide an output
referencing the physics grid itself.

This allows you to do things like rotation, transformation or teleportation
of the physics grid the *Read Brick Grid* gate is on.
