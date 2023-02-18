import math
import pcbnew
import kicad_turtle


board = pcbnew.LoadBoard('pcb_with_nets.kicad_pcb')


t =  kicad_turtle.KicadPcbTurtle(board,130,100,0)

t.setNet("AAA")
t.setWidth(2)
t.penDown()
t.forward(10)
t.penUp()
t.setNet("")
t.setLayerName("B.Cu")
t.forward(10)
t.penDown()
t.forward(10)


board.Save('turtle-example4.kicad_pcb')

