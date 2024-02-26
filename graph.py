# This program makes a simple 2d scatter plot in the 1st quadrant with graph().
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #This suppresses the annoying PyGame welcome message
import pygame
import random #For randtable()

# Generate a list of two lists of points; the y vals are random but the xvals are equidistant. Goes through the origin.
def randtable(dim, xmax, ymax):
	xlist = [0]
	ylist = [0]
	for count in range(1,dim):
		xlist = xlist + [xmax*count/dim]
		ylist = ylist + [random.uniform(0,ymax)]
	return[xlist,ylist]
	# Note that this returned a nested list. So you reference it like so: result[number][number]


# Parameters are screen width and length (by pixels), the x values list, and the y values list
def grapher(screen_size,lines,combined_x_and_y_lists):
	x_list = combined_x_and_y_lists[0]
	y_list = combined_x_and_y_lists[1]
	# manage error conditions
	if min(x_list) < 0:
		exit("Item less than zero.")
	if min(y_list) < 0:
		exit("Item less than zero.")
	if len(x_list) != len(y_list):
		exit("X and Y lists not the same length.")
	max_x = max(x_list)
	max_y = max(y_list)
	
	# initialize the pygame module
	pygame.init()
	# create a surface on screen of a certain size (pixels)
	my_screen = pygame.display.set_mode((screen_size,screen_size))

	# change background color
	my_screen.fill((0,20,20))

	# draw the axis lines (note that this function locates pixels as (rightward,downward)
	pygame.draw.line(my_screen,(200,220,0),(int(screen_size*0.1),int(screen_size*0.1)) , (int(screen_size*0.1),int(screen_size*0.9)))
	pygame.draw.line(my_screen,(200,220,0),(int(screen_size*0.1),int(screen_size*0.9)) , (int(screen_size*0.9),int(screen_size*0.9)))

	# Draw all points, and make them thick
	for count in range(0,len(x_list)):
		print("Graphing point [" , x_list[count] , "," , y_list[count] , "]")

		x_location = 0.1+0.8*(x_list[count]/max_x)
		y_location = 0.9-0.8*(y_list[count]/max_y)

		for pixel_widening in range(-2,3):
			for pixel_lengthening in range(-2,3):
				if not(abs(pixel_widening) == 2 and abs(pixel_lengthening) == 2): # This will round the points instead of making them 5x5 squares
					# Note how below, the "draw.line" function isn't used to draw a line but only one point (one pixel)
					pygame.draw.line(my_screen,(200,150,0), (pixel_widening+int(screen_size*x_location),pixel_lengthening+int(screen_size*y_location)) , (pixel_widening+int(screen_size*x_location),pixel_lengthening+int(screen_size*y_location))    )

		# Draw a skinny line to the next dot starting from the current thick dot. Don't try drawing a line starting at the final point
		if lines and count!=len(x_list)-1:
			x_location2 = 0.1+0.8*(x_list[count+1]/max_x)
			y_location2 = 0.9-0.8*(y_list[count+1]/max_y)
			pygame.draw.line(my_screen,(200,100,40), ( int(screen_size*x_location) , int(screen_size*y_location) ) , (int(screen_size*x_location2) , int(screen_size*y_location2) ) )
			

	# render the whole screen
	pygame.display.flip()

  	# keep screen open until user quits
	keep_running = True
	while keep_running:
	        for event in pygame.event.get():
	            # only do something if the event is type QUIT
	            if event.type == pygame.QUIT:
	                keep_running = False
