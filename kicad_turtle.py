import math
import pcbnew

class KicadPcbTurtle:

    SCALE = 1000000
    NET = ''
    WIDTH = 0.3
    LAYERNAME = 'F.Cu'

    def __init__(self, board, x, y, heading):
        self.board = board
        self.xpos = x
        self.ypos = y
        self.heading = heading
        self.pendown = True

    def setLayerName(self, layername):
        self.LAYERNAME = layername

    def setNet(self, net):
        self.NET = net

    def setWidth(self, width):
        self.WIDTH = width

    def forward(self, pixels):
        radians = self.heading * math.pi / 180.0
        dx = math.cos(radians) * pixels
        dy = math.sin(radians) * pixels
        self.goto_real(self.xpos + dx, self.ypos + dy)

    def backward(self, pixels):
        self.forward(-pixels)

    def goto_real(self, x, y):
        if (self.pendown == True):
            item = pcbnew.PCB_TRACK(self.board)
            item.SetWidth(int(self.WIDTH*self.SCALE))
            item.SetStart(pcbnew.wxPoint(
                self.xpos*self.SCALE, self.ypos*self.SCALE))
            item.SetEnd(pcbnew.wxPoint(x*self.SCALE, y*self.SCALE))
            layerid = self.board.GetLayerID(self.LAYERNAME)

            if(layerid!=-1):
                item.SetLayer(layerid)
            else:
                print ('hiba')
                exit(1)

            net = self.board.GetNetsByName()

            if(self.NET!=''):
                item.SetNet(net["/"+self.NET])

            self.board.Add(item)
        self.xpos = x
        self.ypos = y

    def penUp(self):
        self.pendown = False

    def penDown(self):
        self.pendown = True

    def turn_left(self, angle):
        self.heading += angle
        if (self.heading < 0.0):
            self.heading += 360.0
        elif (self.heading >= 360.0):
            self.heading -= 360.0

    def turn_right(self, angle):
        self.turn_left(-angle)
