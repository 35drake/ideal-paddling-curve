# This program calculates the ideal paddling curve

import os
from graph import grapher #The grapher() function
from graph import randtable
from paddling_math import paddling_time
from paddling_math import normalize
from paddling_math import debug_area_find



# Step 0: Initialize the program
# -----------------------------------------
# Variables to set:
dimension = 5 
x_max = 1
y_max = 5
factor = 0.26 # This represents what fraction of the Force vs. Distance graph we're allowed to occupy. Essentially it determines the paddler's total energy. Literally, the physics equation "E=d*F" applies as "TotalEnergy = factor * x_max * y_max" . 
# NOTE: additional variables are set in beginning of yellow()


# Calculate total paddler energy (aka graph area under the curve)
Energy = x_max * y_max * factor # We're gonna use this variable to normalize graphs, so that their area under the curve is actually this value

# This list of list of pairs of lists, will house all the graphs that we try.
# Example: The full thing might look like [ [[0,1,2],[0.4,0.3,0.5]] , [[0,1,2],[0.2,0.6,0.2]] ]
#	An x_list or y_list from one graph will look like [0,1,2]
#	Together a x_list and y_list make up a graph's full data set, like this [[0,1,2],[0.4,0.3,0.5]]
#	The full graphs_list is a list of those full data sets from every graph
graphs_list = [] #This will be a 3d array. Reference it like so: graphs_list[graph number][ x or y list (use 0 for x and 1 for y) ][point number]

# NOTE: graphs_list will not contain every graph we try. Only the best graphs so far. So, after the program's done, each graph stored in this list will be better than the prev.

#demo to show how to reference graphs_list:
#graphs_list = graphs_list + [randtable(dimension,1,5)]
#graphs_list = graphs_list + [randtable(dimension,1,5)]
#print(graphs_list)
#print(graphs_list[1][1][3])
#exit()


# Step 1: generate a random graph to start with
# -----------------------------------------


graphs_list = graphs_list + [ normalize(Energy, randtable(dimension,x_max,y_max)) ]
# Show off the graph that was just created
grapher(800,True,graphs_list[0])

# Double check that its area is correct
print(debug_area_find(graphs_list[0]) , "should be be approx" , Energy)



# Calculate the paddling time of this graph
best_time_so_far = paddling_time(graphs_list[0])
print("Time of this original graph is",best_time_so_far)
# Note: we don't need to keep an index to keep track of which graph in graphs_list has been the best so far, BECAUSE the last graph in it is the best. We won't add inferior graphs to grahps_list[]


# Step 2: Alter the current/best graph slightly, by moving one point up then down. Start with the first point and move onto the next point and so on. When a point change makes a superior graph, then set that graph to be the new current graph, and start this step over again. If you end up changing all points up/down but have never made a superior graph, then we're done.
# -----------------------------------------



# Step 3: 
# -----------------------------------------

# Step 4:
# -----------------------------------------











#grapher(800,True,randtable(10,4,6))
#grapher(800,True,[[0,1,2,3,4],[5,2,5,8,6]])