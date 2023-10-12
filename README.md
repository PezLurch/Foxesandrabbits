# Wildlifesimulation

This "simulates" some sort of "natural situation":

There are foxes and rabbits. They are being printed onto a window using pygame. 

The foxes eat the rabbits when they are close enough to them and when their stomach is not empty. 
Eating a rabbit adds +1 to the stomache attribute of the fox (and removes the rabbit from the game). 

If the stomach is empty, the fox dies.

There is also gras which regrows at a certain pace. The rabbits can eat of the gras which reduces it. 
Also here, eating gras makes stomach += 1 and in case the stomach is empty, the rabbit dies. 

It's not completely thought throw but quite a lot of fun to play around with the parameters 
to see if the foxes kill all rabbits and then die of hunger, or die of hunger and only rabbits remain
or if there is some sort of sustainable system. 
