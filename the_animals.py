'''
This file contains the class Animal and 
its subclasses Fox and Rabbit.
'''
import math
import pygame
import random
import sys
import time 
import sys
import time 
from random import randint as randint
import matplotlib.pyplot as plt


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
    def __init__(self, posx, posy, dirx, diry,speed,screensize,stomach):
        self.posx = posx
        self.posy = posy
        self.dirx = dirx
        self.diry = diry
        self.speed = speed
        self.screensize = screensize
        self.stomach = stomach

    def moveanimal(self):
        self.posx += self.dirx
        self.posy += self.diry
        return self
    
    def updatedirection_det(self):
        if self.posx >= self.screensize - self.speed:
            self.dirx = -self.speed#random.randint(-self.speed,0)
        elif self.posx <= self.speed:
            self.dirx = self.speed#random.randint(0,self.speed)

        
        if self.posy >= self.screensize - self.speed:
            self.diry = -self.speed#random.randint(-self.speed,0)
        elif self.posy <= self.speed:
            self.diry = self.speed#random.randint(0,self.speed)



    def updatedirection(self):
        ##TO DO: MAKE THIS LOOK MORE NATURAL
        
        if self.posx >= self.screensize - self.speed:
            self.dirx = -self.speed#random.randint(-self.speed,0)
        elif self.posx <= self.speed:
            self.dirx = self.speed#random.randint(0,self.speed)
        else: 
            self.dirx = random.randint(-self.speed,self.speed)
        
        if self.posy >= self.screensize - self.speed:
            self.diry = -self.speed#random.randint(-self.speed,0)
        elif self.posy <= self.speed:
            self.diry = self.speed#random.randint(0,self.speed)
        else:
            self.diry = random.randint(-self.speed,self.speed)
        return self 
    
    def draw_animal(self,screen):
        pygame.draw.circle(screen, pygame.Color(self.color), [self.posx, self.posy], 5)
    

    def digest(self):
        self.stomach -= 1
        return self.stomach



class Fox(Animal):
    def __init__(self,posx, posy, dirx, diry,speed,screensize,stomach):
        Animal.__init__(self,posx, posy, dirx, diry,speed,screensize,stomach)
        self.color = (128,0,0)
    
    def is_close(self,rabbit,safety_distance=10):
        return math.sqrt((self.posx - rabbit.posx)**2 + (self.posy - rabbit.posy)**2) < safety_distance
    
    


class Rabbit(Animal):
    def __init__(self,posx, posy, dirx, diry,speed,screensize,stomach):
        Animal.__init__(self,posx, posy, dirx, diry,speed,screensize,stomach)
        self.color = (255,255,255)



def create_random_fox(screensize,fox_speed):
    return Fox(randint(0,screensize),randint(0,screensize),15,15,fox_speed,screensize,0)

def create_random_rabbit(screensize,rabbit_speed):
    return Rabbit(randint(0,screensize),randint(0,screensize),15,15,rabbit_speed,screensize,0)


def reproduce(rate,amount):
    return randint(0,amount) if randint(0,rate) == 1 else 0


def plot_populations_and_gras(track_fox_population,track_rabbit_population,track_gras):
    plt.plot(track_fox_population, label = "foxes")
    plt.plot(track_rabbit_population, label = "rabbits")
    plt.plot(track_gras, label = "gras")
    plt.legend()
    plt.show()


def rand_fox_speed(fox_speed):
    return randint(1,fox_speed)
