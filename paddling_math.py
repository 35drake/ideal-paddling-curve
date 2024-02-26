# This function modifies a graph to be normalized to have the correct area under the curve
def normalize(desired_area,my_graph):
	# Grab the dimension of the graph (aka the number of points) cuz it wasn't passed
	dimension = len(my_graph[0])
	# print(dimension)
	
	# Find the current area
	current_area = 0	
	# Use the trapezoidal rule for every segment
	for point in range(0,dimension-1): # The "minus one" exists because the final point has no trapezoid to the right of it; that's the edge of the graph
		x_span = my_graph[0][point+1] - my_graph[0][point] # How wide the trapezoid is (this should actually be a constant value but I'll calculated it in every iteration anyway). Note that the zeroes here refer to grabbing x values instead of y values (the array would be indexed by 1's)
		y_avg = 0.5 * ( my_graph[1][point] + my_graph[1][point+1] )
		current_area = current_area + x_span * y_avg
	

	#Amplify all y point values by this factor, so that the area under the curve is now correct
	amplification = desired_area / current_area
	for point in range(0,dimension): # No "minus one" this time cuz we need to hit every point
		my_graph[1][point] = amplification * my_graph[1][point] #Only do the y points. Don't do the x points because we don't need to shrink the graph that way.
	
	# print(my_graph)
	return my_graph

# This debug function finds the area under your graph. You basically use it to ensure that normalize() worked correctly.	
def debug_area_find(my_graph):
	# Grab the dimension of the graph (aka the number of points) cuz it wasn't passed
	dimension = len(my_graph[0])
	
	# Find the current area
	current_area = 0
	# Use the trapezoidal rule for every segment
	for point in range(0,dimension-1): # The "minus one" exists because the final point has no trapezoid to the right of it; that's the edge of the graph
		x_span = my_graph[0][point+1] - my_graph[0][point] # How wide the trapezoid is (this should actually be a constant value but I'll calculated it in every iteration anyway). Note that the zeroes here refer to grabbing x values instead of y values (the array would be indexed by 1's)
		y_avg = 0.5 * ( my_graph[1][point] + my_graph[1][point+1] )
		current_area = current_area + x_span * y_avg
	return current_area


# This function takes a graph/table of values, and calculates the total paddling time
def paddling_time(my_graph):
	# my_graph looks like [ [0,1,2][0,0.5,0.6] ] or something. Dim could be anything though. As in the dimensions are as such: my_graph[2,?]
	
	# Grab the dimension of the graph (aka the number of points) cuz it wasn't passed
	dimension = len(my_graph[0])

	# Find the width of each graph region
	xspan = my_graph[0][1] - my_graph[0][0]

	# Initialize before we go into the for loop
	v0 = 0 #This doesn't actually represent initial velocity of the whole graph, but initial velocity of the current step / yellow region. So, for now v0 represents v(t=0), but it won't always be that way.
	time_total_so_far = 0 #This will be increased every yellow region
	
	# Loop through every yellow region, to find how long the paddler spent in that region, and also their new velocity coming out of that region
	for region in range(0,dimension-1): #note that there is 1 more pair of points than there are graph regions
		yellow_output = yellow(v0,xspan,my_graph[1][region],my_graph[1][region+1]) #Bulk of the math is done with yellow()
		v0 = yellow_output[0] #this is the final velocity output by yellow()
		time_total_so_far = time_total_so_far + yellow_output[1]

	return time_total_so_far

# This is a subfunction of paddling_time(). It represents the yellow region of my Google Docs paper. It outputs the final velocity and total paddling time so far, at the end of this yellow region.
def yellow(v0, xspan, y0, yf):
	# SET THE IMPORTANT VARIBLES
	m = 100 #paddler mass
	B = 4.1 #drag factor
	steps = 30 #how many iterations you wanna do for a yellow region

	# calculate the variable "A", see Google Document for what this refers to
	A = (yf - y0) / xspan
	# note that at any point in this yellow region, y = y0 + (yf - y0)/xspan * d, or ... y = A * d


	# initialize the v list; this will hold every velocity along the yellow region, including the end velocity
	v = [-41] * (steps + 1) # negative 41 is just a placeholder value
	v[0] = v0

	# initialize the v-squared list; this holds all the squares of the velocities found so far. Note: since I'm using sum(), it's important that this list is initialized with zeroes
	# We have to keep a list of v-squared's and not just the current value, because of how we're iterating over the intergral of v-squared.
	v_squared = [0] * (steps+1)
	v_squared[0] = v0**2 #clearly zero but I added the line for clarity

	# iterate through the whole yellow region to acquire the list of all the paddler's velocities after each iteration. Since the real velocity equation is complicated, we're going to iterate and find the next v value by using the previous v value in the calculation.
	for count in range(0,steps):

		# Find the integral of all the v-squared's that have been found so far. Basically a Riemann sum, where each Riemann piece has width of xspan/steps. In theory we shouldn't sum the whole v-squared list, but only up to the current value. But I don't care since any future values are still 0 for now.
		integral = xspan / steps * sum(v_squared)

		# Find the little d, which is the distance gone so far into the yellow region
		d = xspan / steps * count

		# Iterate to get the next velocity, using the current velocity
		# v[count+1] = equation that uses v[count]
		v[count+1] = ( v0**2 + 2*y0*d/m + A*d*d/m - 2*B/m*integral ) ** 0.5
		v_squared[count+1] = v[count+1]**2	

	t_spent_here = 41
	# use the list of velocities to find t_spent_here (hint: it's the area under the "1/v vs d" curve)
	pass



	# return [v_final,t_spent_here]
	return [v[steps],t_spent_here] #Note that v[steps] exists and is the final item in v[]





