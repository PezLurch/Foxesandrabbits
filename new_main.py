import math
import pygame
import random
import sys
import time 

from the_animals import Animal,Fox, Rabbit

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1000, 1000))

    fox = Fox(500,500,0,0,0)
    rabbit = Rabbit(600,600,0,0,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill((22, 185, 30))
        fox.draw_animal(screen)
        rabbit.draw_animal(screen)
        fox.moveanimal(1000)
        rabbit.moveanimal(1000)
        fox.updatedirection(1000)
        print(fox.posx, fox.posy)
        rabbit.updatedirection(1000)
        clock.tick(280)
        pygame.display.flip()

if __name__ == "__main__":
    main()
