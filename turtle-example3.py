import math
import pcbnew

import kicad_turtle

board = pcbnew.LoadBoard('empty.kicad_pcb')


i = 1
r = 0.00003
s = 0.1
t = kicad_turtle.KicadPcbTurtle(board, 130, 100, 0)
while i < 400*10:
    t.forward(s)
    t.turn_left(1)
    s += r
    i += 1


board.Save('turtle-example3.kicad_pcb')
