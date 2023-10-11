import random
import math

class Fox():

    def __init__(self, posx, posy, dirx, diry, stomach):
        self.posx = posx
        self.posy = posy
        self.dirx = dirx
        self.diry = diry
        self.stomach = stomach
        self.condition = True
        self.color = (128,0,0)
    
    def movefox(self, windowsize):
        self.posx += self.dirx
        self.posy += self.diry
        return self

    def updatedirection(self, windowsize):
        if self.dirx == 0 and self.diry == 0:
            self.dirx = 1
            self.diry = 1
        if self.dirx < 0:
            if self.posx < 10:
                self.dirx = -(self.dirx + random.randint(-5,0))
        elif self.dirx > 0:
            if self.posx > windowsize - 10:
                self.dirx = -(self.dirx + random.randint(0,5))
        if self.diry < 0:
            if self.posy < 10:
                self.diry = -(self.diry + random.randint(-5,0))
        elif self.diry > 0:
            if self.posy > windowsize - 10:
                self.diry = -(self.diry + random.randint(0,5))
        if self.dirx < -10:
            self.dirx =-5
        if self.dirx > 10:
            self.dirx =5
        if self.diry < -10:
            self.diry =-5
        if self.diry > 10:
            self.diry =5
        return self

    def printposition(self):
        print("Current position: ",self.posx, self.posy)
    
    
class Rabbit():
    def __init__(self,posx, posy, dirx, diry):
        self.posx = posx
        self.posy = posy
        self.dirx = dirx
        self.diry = diry
        self.condition = True
        self.color = (255,255,255)


    def moverabbit(self, windowsize):
        self.posx += self.dirx
        self.posy += self.diry
        return self

    def updatedirection(self, windowsize):
        if self.dirx == 0 and self.diry == 0:
            self.dirx = 1
            self.diry = 1
        if self.dirx < 0:
            if self.posx < 10:
                self.dirx = -(self.dirx + random.randint(-5,0))
        elif self.dirx > 0:
            if self.posx > windowsize - 10:
                self.dirx = -(self.dirx + random.randint(0,5))
        if self.diry < 0:
            if self.posy < 10:
                self.diry = -(self.diry + random.randint(-5,0))
        elif self.diry > 0:
            if self.posy > windowsize - 10:
                self.diry = -(self.diry + random.randint(0,5))
        if self.dirx < -10:
            self.dirx =-5
        if self.dirx > 10:
            self.dirx =5
        if self.diry < -10:
            self.diry =-5
        if self.diry > 10:
            self.diry =5
        return self

    
