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
fox_speed = 15
fox_digest_time = 30
fox_breed_rate = 100
fox_breed_amount = 3

rabbit_breed_time = 5
rabbit_breed_rate = 10
rabbit_breed_amount = 5
rabbit_speed = 15
rabbit_digest_time = 10

max_new_gras = 40
safety_distance = 7


#setup in the beginning
number_of_foxes = 10
number_of_rabbits = 60



def create_random_fox():
    return Fox(randint(0,screensize),randint(0,screensize),0,0,fox_speed,screensize,0)

def create_random_rabbit():
    return Rabbit(randint(0,screensize),randint(0,screensize),0,0,rabbit_speed,screensize,0)

def reproduce(rate,amount):
    return randint(0,amount) if randint(0,rate) == 1 else 0




def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screensize, screensize))
    #TO DO: Make nice sliders to control the global variables!
    #slider = Slider(screen, 100, 100, 100, 40, min=0, max=99, step=1)
    #output = TextBox(screen, 475, 200, 50, 50, fontSize=30)

    foxes = [create_random_fox() for _ in range(number_of_foxes)]
    rabbits = [create_random_rabbit() for _ in range(number_of_rabbits)]
    
    #variables that are changed within the simulation have to be defined within the main function
    index = 0
    food = 1000

    #The following arrays collecect the data for the graph that we can look at by pressing space.
    total_foxes = [len(foxes)]
    total_rabbits = [len(rabbits)]
    total_food = [food]


    while True:
        index += 1
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
                plt.plot(total_foxes, label = "foxes")
                plt.plot(total_rabbits, label = "rabbits")
                plt.plot(total_food, label = "food")
                plt.legend()
                plt.show()
        

        screen.fill((52, 185, 30))
        
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

        
        for rabbit in rabbits:
            if rabbit.stomach < 0:
                rabbits.remove(rabbit)
        

        for rabbit in rabbits:
            if food > 0:
                if rabbit.stomach <=3:
                    rabbit.stomach += 1
                    food -= 1
            else: break
        
        food += randint(0,max_new_gras)



        for fox in foxes:
            if fox.stomach < 0:
                foxes.remove(fox)
            if fox.stomach <= 3:
                for rabbit in rabbits:
                    if fox.is_close(rabbit,safety_distance):
                        rabbits.remove(rabbit)
                        fox.stomach += 1
                        break
            else:
                foxes += [Fox(randint(0,screensize),randint(0,screensize),0,0,fox_speed,screensize,0) 
                    for _ in range(reproduce(fox_breed_rate,fox_breed_amount))]

        for fox in foxes:
            fox.updatedirection()
            fox.moveanimal()
            fox.draw_animal(screen)
        for rabbit in rabbits:
            rabbit.updatedirection()
            rabbit.moveanimal()
            rabbit.draw_animal(screen)
        #print(len(foxes),len(rabbits), foxes[0].dirx, foxes[0].diry)

        total_foxes.append(len(foxes))
        total_rabbits.append(len(rabbits))
        total_food.append(food)

        clock.tick(200)
        #output.setText(slider.getValue())

        #pygame_widgets.update(events)
        pygame.display.flip()

if __name__ == "__main__":
    main()
