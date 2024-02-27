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
tweak_ratio = 1.01 #This (and its multiplicative inverse) are the ratios by which points will increase their y values when tweaked
x_max = 1
y_max = 5
factor = 0.26 # This represents what fraction of the Force vs. Distance graph we're allowed to occupy. Essentially it determines the paddler's total energy. Literally, the physics equation "E=d*F" applies as "TotalEnergy = factor * x_max * y_max" . 
loud = False #If you want output from THIS program
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
grapher("x",800,True,graphs_list[0])

# Double check that its area is correct
if loud:
	print("\nThe total paddler energy on this graph is", debug_area_find(graphs_list[0]) , " which should be be approx" , Energy)


# Calculate the paddling time of this graph
best_time_so_far = paddling_time(graphs_list[0])



if loud:
	print("Time of this original graph is",best_time_so_far)
# Note: we don't need to keep an index to keep track of which graph in graphs_list has been the best so far, BECAUSE the last graph in it is the best. We won't add inferior graphs to graphs_list[]


# Step 2: Tweak current/best graph slightly, by moving one point up then down. Start with the first point and move onto the next point and so on. When a point change makes a superior graph, then set that graph to be the new current graph, and start this step over again. If you end up changing all points up/down but have never made a superior graph, then we're done.
# -----------------------------------------

# Note that graphs_list[] holds all our best graphs so far. Meaning that graphs_list[len(graphs_list)] will always hold the currently-best-ever graph.
# Now let's tweak the graph, one point at a time and one sign at a time (tweaking down or up). 
# We'll know we have the final graph when none of the tweaks work through the entire big for loop (we had a full "perfect run"). See variable below:

potentially_perfect_run = False #This variable has no meaning yet; it's just set to False so we can enter the while loop
while potentially_perfect_run == False: #We're gonna loop through this loop until we have a graph that cannot be tweaked to become better; it's already perfect
	potentially_perfect_run = True # The run has NOT proven to be perfect yet, but if it survives the whole for loop below as True, then we're done and happy
	for point in range(0,dimension):
		for sign in [-1,1]:
			this_tweak_failed_so_lets_move_on = False #This will remain false until the tweak produces a WORSE graph than our current; instead of a better one 
			while this_tweak_failed_so_lets_move_on == False: #If a tweak (ie move point 7 up by ratio of tweak_ratio) works, we're gonna keep doing it again and again till it fails
				
				# Make a temporary testing_graph for us to see if it beats the current graph, which is graphs_list[-1] aka the most recent graph on it
				testing_graph = graphs_list[-1] 
				testing_graph[1][point] = testing_graph[1][point] * tweak_ratio**sign #tweak it. By changing just one y value
				testing_graph = normalize(Energy, testing_graph) #Normalize it
				
				# get this tweaked graph's paddling time
				testing_time = paddling_time(testing_graph)

				# see if this tweak has success (aka the lowest paddling time so far)
				if testing_time < best_time_so_far:
					# make it the new latest graph in graphs_list. Note that we're gonna try this exact same tweak again after this, since it succeeded. Ie, if decreasing point #6 worked, then we'll keep trying it again and saving new graphs into graphs_list[] until it stops working
					graphs_list = graphs_list + [testing_graph]
					# set the new best paddling time, corresponding to the new best graph we just got
					best_time_so_far = testing_time
					print(best_time_so_far,"sec")
					# note that this run is not a perfect run, so the old graph was not the end solution
					potentially_perfect_run = False
				else:
					# move on to the next tweak
					this_tweak_failed_so_lets_move_on = True
			
				
# The solution graph now exists in graphs_list[-1]
# Flash through all best-so-far solutions found (nvm thats way too many; better to only display a graph when it was a big jump, ie an improvement of 0.2sec or more)
#for my_graph in graphs_list:	
#	grapher(0.01,800,True,my_graph)





# Step 3: Show the best graph made, and even show some text on the graph image. 
# -----------------------------------------



# Step 4:
# -----------------------------------------











#grapher("x",800,True,randtable(10,4,6))
#grapher("x",800,True,[[0,1,2,3,4],[5,2,5,8,6]])