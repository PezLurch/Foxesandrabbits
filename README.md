# Wildlifesimulation

This is a project I did as a student. It "simulates" and visualizes the following set up:

There are foxes and rabbits. Their positions are being visualized with circles in a window. 

The following things happen:
 - The foxes eat the rabbits when they are close enough to them and when their stomach is not full. 
   Eating a rabbit adds +1 to the stomache attribute of the fox (and removes the rabbit from the game). 

 - If the stomach of a fox or a rabbit is empty, the fox/rabbit dies.

 - There is also gras which regrows at a certain pace. The rabbits can eat of the gras which reduces it. 
   Also here, eating gras makes stomach += 1 and in case the stomach is empty, the rabbit dies. 

 - Rabbits and foxes reproduce at some rate (can be specified in new_main.py) when their stomach is sufficiently full.

 - Pressing the space bar, we get a matplotlib plot showing the population development so far.

This is a screenshot of how it looks.

<center><img width="506" alt="Screenshot 2023-10-16 at 15 24 11" src="https://github.com/PezLurch/Foxesandrabbits/assets/36110820/aadb3939-6767-4a07-93ae-0024e2b4ba4d"></center>


   
It's not completely thought. The intention is to play around with the parameters and see under which conditions this system is stable and under which it "collapses".
