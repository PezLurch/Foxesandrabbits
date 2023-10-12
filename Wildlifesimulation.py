import pygame, sys, random, time
from Animals import Fox, Rabbit
from Wildlife import *
import matplotlib.pyplot as plt

windowsize = 1000
quantityone = 10
quantitytwo = 10
stepsizeone = 10
stepsizetwo = 10
reproductionthreshold = 3
rabbitreproductionmax = 4
foxreproductionmax = 7
maxpop = 10


wildlife = Wildlife(quantityone, quantitytwo, windowsize, reproductionthreshold)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((windowsize, windowsize))
    
    round = 1
    while True:
        if len(wildlife.rabbits) == 0:
            plt.legend()
            plt.show()
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    plt.legend()
                    plt.show()
        round += 1
        
        wildlife.moveanimals(stepsizeone, stepsizetwo, windowsize, round, foxreproductionmax, rabbitreproductionmax, maxpop)
        wildlife.hunt()
        
        wildlife.drawmeadow(screen)
        if round%10 == 0:
        #If we dont use the next if-else sequence, there will be as many legends as datapoints...
            if round != 10:
                plt.plot(round, len(wildlife.rabbits), 'ro')
                plt.plot(round, len(wildlife.foxes), 'bo')
            else:
                plt.plot(round, len(wildlife.rabbits), 'ro', label = "rabbits")
                plt.plot(round, len(wildlife.foxes), 'bo', label = "foxes")
        print(len(wildlife.foxes))
        clock.tick(280)
        pygame.display.flip()
    

main()

