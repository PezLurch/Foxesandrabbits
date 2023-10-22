import math
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import random
import sys
import time 
from random import randint as randint
import matplotlib.pyplot as plt

from the_animals import Animal, Fox, Rabbit

#global variables
screensize = 500
fox_speed = 10
fox_digest_time = 20
fox_max_stomach = 3
fox_breed_rate = 100
fox_breed_amount = 3

rabbit_breed_time = 5
rabbit_breed_rate = 10
rabbit_breed_amount = 5
rabbit_speed = 15
rabbit_digest_time = 10

max_new_gras = 70
safety_distance = 4

population_tracking_rate = 10

#setup in the beginning
number_of_foxes = 40
number_of_rabbits = 50



def create_random_fox():
    return Fox(randint(0,screensize),randint(0,screensize),15,15,fox_speed,screensize,0)

def create_random_rabbit():
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

def main():
    #Set up pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screensize, screensize))

    #TO DO: Make nice sliders to control the global variables! Something like this:

    #slider = Slider(screen, 100, 100, 100, 40, min=0, max=99, step=1)
    #output = TextBox(screen, 475, 200, 50, 50, fontSize=30)
    #output.setText(slider.getValue())
    #pygame_widgets.update(events)


    #create random lists of foxes and rabbits
    foxes = [create_random_fox() for _ in range(number_of_foxes)]
    rabbits = [create_random_rabbit() for _ in range(number_of_rabbits)]
    
    #variables that are changed within the simulation have to be defined within the main function
    index = 0
    gras = 100

    #The following arrays collecect the data for the graph that we can look at by pressing space.
    track_fox_population = [len(foxes)]
    track_rabbit_population = [len(rabbits)]
    track_gras = [gras]


    while True:
        index += 1
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
                plot_populations_and_gras(track_fox_population,track_rabbit_population,track_gras)

        #only animals with food in the stomach survive. 
        rabbits = [rabbit for rabbit in rabbits if rabbit.stomach >= 0]
        foxes = [fox for fox in foxes if fox.stomach >= 0]
        
        
        if index % fox_digest_time == 0:
            for fox in foxes:
                fox.digest()
        if index % rabbit_digest_time == 0:
            for rabbit in rabbits:
                rabbit.digest()
    


        if index % rabbit_breed_time == 0:
            for rabbit in rabbits:
                rabbits += [Rabbit(randint(0,screensize),randint(0,screensize),0,0,rabbit_speed,screensize,0) 
                    for _ in range(reproduce(rabbit_breed_rate,rabbit_breed_amount))]

        


        #shuffle the rabbits so a random subset gets gras!
        random.shuffle(rabbits)

        for rabbit in rabbits:
            if gras > 0 and rabbit.stomach <= 3:
                rabbit.stomach += 1
                gras -= 1
            else: break
        

        #let new gras grow
        gras += randint(0,max_new_gras)

        for fox in foxes:
            if fox.stomach <= fox_max_stomach:
                for rabbit in rabbits:
                    if fox.is_close(rabbit,safety_distance):
                        rabbits.remove(rabbit)
                        fox.stomach += 1
                        break
            else: #if stomach of fox is full: they might breed. 
                foxes += [Fox(randint(0,screensize),randint(0,screensize),rand_fox_speed(fox_speed),rand_fox_speed(fox_speed),fox_speed,screensize,0) 
                    for _ in range(reproduce(fox_breed_rate,fox_breed_amount))]



        screen.fill((52, 185, 30))
        for fox in foxes:
            fox.updatedirection()
            fox.moveanimal()
            fox.draw_animal(screen)
        for rabbit in rabbits:
            rabbit.updatedirection()
            rabbit.moveanimal()
            rabbit.draw_animal(screen)

        
        if index %population_tracking_rate == 0:
            track_fox_population.append(len(foxes))
            track_rabbit_population.append(len(rabbits))
            track_gras.append(gras)

        clock.tick(200)
       
        pygame.display.flip()

if __name__ == "__main__":
    main()
