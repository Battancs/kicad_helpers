import math
import pcbnew

import kicad_turtle

board = pcbnew.LoadBoard('empty.kicad_pcb')

#board = pcbnew.LoadBoard('test1.kicad_pcb')







i = 1
r = 0.3
s = 10
t =  kicad_turtle.KicadPcbTurtle(board,100,100,0)
while i < 40:
	t.forward(s)
	t.turn_left(88)
	s+=r
	i+=1


# t =  kicad_turtle.KicadPcbTurtle(board,130,100,0)


# # board.


# # map = pcbnew.NETNAMES_MAP(board)

# t.setNet("AAA")
# t.setWidth(2)
# t.penDown()
# t.forward(10)
# t.penUp()
# t.setNet("")
# t.setLayerName("B.Cu")
# t.forward(10)
# t.penDown()
# t.forward(10)



# i = 1
# r = 0.3
# s = 5
# t =  kicad_turtle.KicadPcbTurtle(board,130,100,0)
# while i < 40:
# 	t.penDown()
# 	t.forward(s)
# 	t.penUp()
# 	t.forward(s)
# 	t.turn_left(88)
# 	s+=r
# 	i+=1



# i = 1
# r = 0.00003
# s = 0.1
# t =  kicad_turtle.KicadPcbTurtle(board,130,100,0)
# while i < 400*10:
# 	t.forward(s)
# 	t.turn_left(1)
# 	s+=r
# 	i+=1




board.Save('turtle-example1.kicad_pcb')


