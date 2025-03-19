#learn-special-methods-by-building-a-vector-space
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-special-methods-by-building-a-vector-space

#In Python, you can enforce the use of keyword-only arguments by adding a * as an additional argument to the function or method signature. 
#Modify both __init__ methods by adding a * as the second parameter (after self). 
#Every parameter placed after that will require the use of a keyword argument in the function/method call.
#This means that you need to modify the super().__init__(x, y) call, too. Do it by giving x the value x, and y the value y.
#Every object in Python has a special attribute named __dict__, which is a dictionary that stores the object attributes.
#As you can see from the output, __dict__ contains the values of your instance attributes. 
#Instead of explicitly adding the squares of self.x and self.y, you are going to iterate over the values stored in __dict__ to calculate the value of the norm.
#Within the norm method body, replace the content of the parentheses with a generator expression that elevates each value val in self.__dict__.values() to the power of 2. 
#Also, pass that generator expression as the argument to the sum function, so that all the squares are added together before calculating the square root.
#The norm() method is returning the correct values, but there's still something you can improve: readability.
#The vars() built-in function takes an object as its argument and returns the __dict__ attribute of that object.
#Instead of directly accessing the __dict__ attribute of self, modify the norm method to use the vars() function.
#When you need to dynamically access some attributes starting from a string input, the built-in getattr() function is what you need. 
#It takes an object as its first argument, and a string containing the attribute name as its second attribute.
#Start to fix the __str__ method by replacing the string returned by __str__() with a generator expression that iterates through the object attributes and calls getattr() for each attribute i.
#While the __str__ method returns a human-readable string representation of an object, the __repr__ method is supposed to return the string needed to instantiate the object.
#The __getattribute__ method is called under the hood any time you try to access an instance attribute. If the attribute is not found at the instance level, the method will search for it at the class level, and eventually in parent classes.

#Inside your class, define a __getattribute__ method with two parameters, self and attr, and make it return the string 'calling __getattribute__'. 
#You'll override momentarily the default implementation just to see how the attribute access works.
#The special method __add__ can be implemented to override what happens by default when two objects are added together using the + operator.
#When adding two vectors, each component of one vector is added to the same component of the other vector. 
#For example, adding (1, 2) and (2, 4) generates a third vector (3, 6), where 3 is the sum of 1 and 2 and 6 is the sum of 2 and 4
#You can unpack a dictionary into keyword arguments by using the ** operator:

#Example Code
#def spam(a, b):
#    return a + b

#my_dict = {a: 11, b: 4}

#spam(**my_dict) # 15
#The special method __mul__ can be implemented to specify what should happen when the current instance is multiplied by another object.
#The __eq__ method can be implemented to specify what should happen in case the comparison operator (==) is used to compare an object with something else.
#The __ne__ method is called under the hood when the != operator is used. 
#The __lt__ method is called under the hood when the < operator is used to compare an object with something else.
#The __gt__ method is called under the hood when the > operator is used to compare an object with something else.
#There are still two possible comparisons to implement. The __le__ method is called when the <= operator is used to compare two objects
#The cross product, or vector product, is defined between 3-dimensional vectors and results in a third vector perpendicular to both of them.
#The cross product between two 3D vectors a and  b can be computed as it follows:
#a×b=⎝aybz−azby
#     azbx−axbz
#     axby−aybx⎞
#Where the resulting vector is represented as a column vector.


class R2Vector:
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
        
    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        return self.__class__(**kwargs)

v1 = R2Vector(x=2, y=3)
v2 = R3Vector(x=2, y=2, z=3)
#print(v1.norm())
#print(v2.norm())
#print(vars(v2).values())
#print(getattr(v2,'x'))
#print(v2.__repr__())
#print(vars(v2).items())
v1 = v1 * 2
print(v1)


v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')