'''
This file contains the class Animal and 
its subclasses Fox and Rabbit.
'''
import math
import pygame
import random
import sys
import time 


class Animal():
    '''
    A class to represent an animal.
    :param posx: The x-coordinate of the animal.
    :param posy: The y-coordinate of the animal.
    :param dirx: The x-direction of the animal.
    :param diry: The y-direction of the animal.
    :param speed: The speed of the animal.
    :param color: The color of the animal.
    :method moveanimal: Moves the animal.
    :method updatedirection: Updates the direction 
    of the animal.
    :method draw_animal: Draws the animal on a screen.
    :method move_animal: Moves the animal.
    '''
    def __init__(self, posx, posy, dirx, diry,speed):
        self.posx = posx
        self.posy = posy
        self.dirx = dirx
        self.diry = diry
        self.speed = speed

    def moveanimal(self, windowsize):
        self.posx += self.dirx
        self.posy += self.diry
        return self
    
    def updatedirection(self, windowsize):
        if self.dirx >= 0 and self.posx <= windowsize - 10:
            self.dirx = random.randint(0,5)
        elif self.posx <= 10:
            self.dirx = random.randint(0,5)
        else:
            self.dirx = random.randint(-5,0)
        if self.diry >= 0 and self.posy <= windowsize - 10:
            self.diry = random.randint(0,5)
        elif self.posy <= 10:
            self.diry = random.randint(0,5)
        else:
            self.diry = random.randint(-5,0)
        return self
    
    def draw_animal(self,screen):
        pygame.draw.circle(screen, self.color, [self.posx, self.posy], 10)



class Fox(Animal):
    def __init__(self,posx, posy, dirx, diry,speed):
        Animal.__init__(self,posx, posy, dirx, diry,speed)
        self.color = (128,0,0)


class Rabbit(Animal):
    def __init__(self,posx, posy, dirx, diry,speed):
        Animal.__init__(self,posx, posy, dirx, diry,speed)
        self.color = (255,255,255)



