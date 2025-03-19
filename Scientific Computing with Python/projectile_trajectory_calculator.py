#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-encapsulation-by-building-a-projectile-trajectory-calculator
#learn-encapsulation-by-building-a-projectile-trajectory-calculator
#You are going to build a program that calculates and draws the trajectory of a projectile given the angle, speed and height of the throw.
#Start by importing math, you will use it a lot in this project as it has useful methods like math.radians, math.cos, math.sin and others.
#The angle provided will be in degrees; however, it should be stored internally in radians. 
#To achieve this, use the math.radians() function to convert the angle from degrees to radians when assigning it to __angle.
#The use of two underscores before an attribute name triggers name mangling in Python. 
#This means the attributes are not directly accessible from outside the class using their given names, and must be accessed with the mangled names like ball._Projectile__height if needed externally, indicating these are intended for internal use only.
#The class variable __slots__ has a special usage in Python classes. Declaring __slots__ and assigning it a sequence of strings restricts the creation of attributes to those included in that sequence. 
#Also, it prevents the creation of the __dict__ special attribute and it allows for more efficient attribute access.


#It's time to talk about encapsulation and getters. You have written the three instance attributes to be private using a leading double underscore. 
#Note that these attributes are called private by convention: although they can still be accessed from outside, it is agreed upon to not do that.
#Getters are what can be used to get the values from outside. To define a getter, you define a method that returns the value of the desired attribute and give it a @property decorator:
#Example Code
	#class Nest:
	#    ...
	#    @property
	#    def number_of_eggs(self):
	#        return self.__number_of_eggs
#The decorator changes the method into a property, meaning that the method is not called like a regular method, but it's used like an attribute:
#Example Code
#n = Nest()
#print(n.number_of_eggs)
#In the example above, the private attribute __number of eggs is accessed through the number_of_eggs property of n


#Once you have the getters, you can write the setters, which allow you to set the value of an attribute in an indirect manner.
#Following the example of the last step, a setter would be written as:
#Example Code
	#class Nest:
	#    ...
	#    @number_of_eggs.setter
	#    def number_of_eggs(self, new_value):
	#        self.__number_of_eggs = new_value
#Same as the getter, a setter is not called like a method but used like an attribute:
#Example Code
	#nest = Nest()
	#nest.number_of_eggs = 12
#This way of writing calls the setter and set the new value.

#The __str__ method refers to the attributes of the class directly, but now that you have created the getters it is better to use those to obtain those values.

#It's good practice to give a representation to the class by using the __repr__ special method. 
#While the __str__ method returns a readable string representation that's intended to be user friendly, __repr__ is intended for programmers. 
#Often __repr__ provides a string that can be used to recreate the object.
#Write the __repr__ method, which will return the string needed to instantiate the object.

import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)
        
    def __str__(self):
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION
        
    def __calculate_y_coordinate(self, x):
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x**2 / (
                2 * self.__speed**2 * math.cos(self.__angle)**2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate

    def calculate_all_coordinates(self):
        return [(x, self.__calculate_y_coordinate(x)) for x in range(0,round(self.__calculate_displacement()))]
        #return [(x, self.__calculate_y_coordinate(x)) for x in range(math.ceil(self.__calculate_displacement()))]        
        
    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        return self.__speed
    
    @height.setter
    def height(self, n):
        self.__height = n

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
       self.__speed = s

    def __repr__(self):
        return f"{self.__class__.__name__}({self.speed}, {self.height}, {self.angle})"      

#Going back to the projectile trajectory calculator, now you'll create a new class that accepts a list of coordinates and creates the trajectory drawing.
#Create a new class Graph, which should be instantiated with a private attribute __coordinates where the list of coordinates is stored. 
#Declare the __slots__ class variable and define the __init__ and __repr__ special methods.       
class Graph:
	__slots__ = ('__coordinates')

	def __init__(self, coord):
		self.__coordinates = coord
    
	def __repr__(self):
		return f'Graph({self.__coordinates})'

	def create_coordinates_table(self):
		table = '\n'
		table += 'x'.rjust(3) + 'y'.rjust(7) + '\n'

		for coord in self.__coordinates:
			x, y = coord
			#y = round(y, 2)
			table += str(x).rjust(3) + f'{y:.2f}'.rjust(7) + '\n'
			#table += f'{x:>3}{y:>7.2f}\n'

		return table

	def create_trajectory(self):
		#make a local copy of the coordinates but where all the values are rounded to integers
		rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]
		#Now that you have the rounded coordinates, find the maximum value between all the x coordinates and the maximum value between all the y coordinates.
		#These max values will be the number of rows and columns in the graph. Save the first in a new variable named x_max and the second in a variable named y_max.
		x_max = max(x for x, _ in rounded_coords)
		y_max = max(y for _, y in rounded_coords)
		#x_max = max(rounded_coords, key=lambda i: i[0])[0]
		#_max = max(rounded_coords, key=lambda j: j[1])[1]		
		#Now that you have x_max and y_max you can use these as number of rows and columns to start building the graph structure: 
		#create a list of lists where the external list contains y_max +1 lists, 
		#each with inside x_max +1 elements, where each element is a string containing a single space.
		#internal_list = [' '] * (x_max + 1)
		#matrix_list = [internal_list] * (y_max + 1)
		matrix_list2 = [[' ' for _ in range(x_max + 1)] for _ in range(y_max + 1)]

		for x, y in rounded_coords:
			matrix_list2[-y-1][x] = PROJECTILE

		#join the internal lists in one string per list
		#matrix_list_new = []
		#for lst in matrix_list2:
		#	matrix_list_new.append(''.join(lst)) 
		matrix_list_new = ["".join(line) for line in matrix_list2]	


		#Add the x and y axes to the graph to obtain the following output:		
		
		matrix_axes = [y_axis_tick + row for row in matrix_list_new]
		matrix_axes.append(" " + x_axis_tick * (len(matrix_list_new[0])))

		graph = "\n" + "\n".join(matrix_axes) + "\n"

		return graph

#ball = Projectile(10, 3, 45)
#print(ball)
#print(ball.calculate_all_coordinates())     
#coordinates = ball.calculate_all_coordinates()
#print(coordinates)
#graph = Graph(coordinates)
#print(graph.create_trajectory())

def projectile_helper(speed, height, angle):
    ball = Projectile(speed, height, angle)
    print(ball)
    coordinates = ball.calculate_all_coordinates()
    graph = Graph(coordinates)
    print(graph.create_coordinates_table())
    print(graph.create_trajectory())    

projectile_helper(10, 3, 45)


# Right-align
#right_aligned = f"{text:>20}"
#print(f"'{right_aligned}'")

# Right-align
#right_aligned = text.rjust(20)
#print(f"'{right_aligned}'")