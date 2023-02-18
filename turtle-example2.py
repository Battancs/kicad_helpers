import math
import pcbnew
import kicad_turtle

board = pcbnew.LoadBoard('empty.kicad_pcb')

i = 1
r = 0.3
s = 5
t =  kicad_turtle.KicadPcbTurtle(board,130,100,0)
while i < 40:
	t.forward(s)
	t.forward(s)
	t.turn_left(90)
	s+=r
	i+=1



board.Save('turtle-example2.kicad_pcb')


