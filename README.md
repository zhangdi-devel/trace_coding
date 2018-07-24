# trace_coding

Two functions were defined:

- `center` finds the center cell index of a garden. If there are multiple center cells, it sorts those cells and return the index of the maximum cell.
- `eat` move the index until there is nowhere to go.

Two concerns:
- The description says each cell is a positive integer, but in the example there are zeros. These initial zeros are considered no carrots as the visied cells.
- If there is tie bwteen any of the four possible next steps, bunny will go for the last one it checks [left, right, up, down].
