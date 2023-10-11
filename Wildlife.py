import random, time, pygame, sys
from Animals import Fox, Rabbit

class Wildlife():
    def __init__(self,quantityone, quantitytwo, windowsize, reproductionthreshold):
        self.quantityone = quantityone
        self.quantitytwo = quantitytwo
        self.windowsize = windowsize
        self.reproductionthreshold = reproductionthreshold
        self.foxes, self.rabbits = self.generateteams()
        self.rabbitmeanx, self.rabbitmeany = self.getrabbitmean()
    

    def givebalance(self):
        print("Remaining foxes: ", len(self.quantityone))
        print("Remaining rabbits: ", len(self.quantitytwo))

    def generateteams(self):
        foxes = []
        rabbits = []
        for index in range(0,self.quantityone):
            fox = Fox(random.randint(0,500), random.randint(0,500), random.randint(-5,5), random.randint(-5,5), random.randint(-5,0))
            foxes.append(fox)
        for index in range(0,self.quantitytwo):
            rabbit = Rabbit(random.randint(0,500), random.randint(0,500), random.randint(-5,5), random.randint(-5,5))
            rabbits.append(rabbit)
        return foxes, rabbits
    
    def drawmeadow(self,screen):
        screen.fill((22, 185, 30))
        for fox in self.foxes:
            pygame.draw.circle(screen, fox.color, [fox.posx, fox.posy], 10)
        for rabbit in self.rabbits:
            pygame.draw.circle(screen, rabbit.color, [rabbit.posx, rabbit.posy], 10)
    
    def moveanimals(self, stepsizeone, stepsizetwo, windowsize, round, foxreproductionmax, rabbitreproductionmax, maxpop):
        for fox in self.foxes: 
            if round%30 == 0:
                fox.stomach -= 1
            if fox.stomach < -15:
                self.foxes.remove(fox)
            elif fox.stomach >14:
                kindlesize = random.randint(0,foxreproductionmax)
                for i in range(0,kindlesize):
                    newfox = Fox(fox.posx + 10, fox.posy + 10,random.randint(-10,10),random.randint(-10,10), 0)
                    fox.stomach = 5
                    self.foxes.append(newfox)
            fox.updatedirection(windowsize)
            fox.movefox(windowsize)
        for rabbit in self.rabbits:
            rabbit.updatedirection(windowsize)
            rabbit.moverabbit(windowsize)
        if len(self.rabbits) < maxpop:
            if len(self.rabbits) != 0:
                number = random.randint(0,len(self.rabbits)-1)
                if number > self.reproductionthreshold:
                    kindlesize = random.randint(0,rabbitreproductionmax)
                    rabbit = self.rabbits[number]
                    for i in range(0,kindlesize):
                        bunny = Rabbit(random.randint(490,510), random.randint(490,510), random.randint(-5,5), random.randint(-5,5))
                        self.rabbits.append(bunny)
        else:
            self.rabbits.pop(0)
        return self
    
    
    def hunt(self):
        for fox in self.foxes:
            for rabbit in self.rabbits:
                if abs(fox.posx - rabbit.posx) < 5 and abs(fox.posy - rabbit.posy) < 5:
                    fox.stomach += 1
                    self.rabbits.remove(rabbit)
                

    
    def getrabbitmean(self):
        meanx = 0
        meany = 0

        for rabbit in self.rabbits:
            meanx += rabbit.posx
            meany += rabbit.posy
        
        if len(self.rabbits) != 0:
            return meanx /len(self.rabbits), meany/ len(self.rabbits) 
        else: return (0,0)
    
    