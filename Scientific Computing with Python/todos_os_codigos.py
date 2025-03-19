# -----------------------------
# Conteúdo de all_the_codes.py
# -----------------------------

import os

diretorio = "./"  # Substitua pelo caminho do seu diretório, se necessário
arquivo_destino = "todos_os_codigos.py"

# Abre o arquivo de destino com a codificação utf-8
with open(arquivo_destino, "w", encoding="utf-8") as destino:
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".py") and arquivo != arquivo_destino:
            destino.write(f"# -----------------------------\n")
            destino.write(f"# Conteúdo de {arquivo}\n")
            destino.write(f"# -----------------------------\n\n")
            # Lê os arquivos com codificação utf-8 também
            with open(os.path.join(diretorio, arquivo), "r", encoding="utf-8") as origem:
                destino.write(origem.read())
                destino.write("\n\n")
print(f"Todos os arquivos Python no diretório foram combinados em {arquivo_destino}!")


# -----------------------------
# Conteúdo de area_calculator.py
# -----------------------------

#In this project you will use object oriented programming to create a Rectangle class and a Square class. 
#The Square class should be a subclass of Rectangle, and inherit its methods and attributes.

##Rectangle class
#When a Rectangle object is created, it should be initialized with width and height attributes. 
#The class should also contain the following methods:

#set_width
#set_height
#get_area: Returns area (width * height)
#get_perimeter: Returns perimeter (2 * width + 2 * height)
#get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
#get_picture: Returns a string that represents the shape using lines of '*'. 
	#The number of lines should be equal to the height and the number of '*' in each line should be equal to the width. 
	#There should be a new line (\n) at the end of each line. 
	#If the width or height is larger than 50, this should return the string: 'Too big for picture.'.
#get_amount_inside: Takes another shape (square or rectangle) as an argument. 
	#Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
	#For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
#Additionally, if an instance of a Rectangle is represented as a string, it should look like: 'Rectangle(width=5, height=10)'.

##Square class
#The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. 
#The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

#The Square class should be able to access the Rectangle class methods but should also contain a set_side method. 
#If an instance of a Square is represented as a string, it should look like: 'Square(side=9)'.

#Additionally, the set_width and set_height methods on the Square class should set both the width and height.

#Usage example
#Example Code
#rect = Rectangle(10, 5)
#print(rect.get_area())
#rect.set_height(3)
#print(rect.get_perimeter())
#print(rect)
#print(rect.get_picture())

#sq = Square(9)
#print(sq.get_area())
#sq.set_side(4)
#print(sq.get_diagonal())
#print(sq)
#print(sq.get_picture())

#rect.set_height(8)
#rect.set_width(16)
#print(rect.get_amount_inside(sq))

#That code should return:
#Example Code
#50
#26
#Rectangle(width=10, height=3)
#**********
#**********
#**********
#81
#5.656854249492381
#Square(side=4)
#****
#****
#****
#****
#8

class Rectangle():

	def set_width(self, w):
		self.width = w

	def set_height(self, h):
		self.height = h

	def __init__(self, w, h):
		self.set_width(w)
		self.set_height(h)

	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'

	def get_area(self):
		return (self.width * self.height)

	def get_perimeter(self):
		return (2 * self.width + 2 * self.height)

	def get_diagonal(self):
		return ((self.width ** 2 + self.height ** 2) ** .5)

	def get_picture(self):
		if self.height > 50 or self.width > 50:
			return 'Too big for picture.'

		line = '*' * self.width + '\n'

		return ''.join([line for _ in range(self.height)])
		
	def get_amount_inside(self, figure):
		return self.get_area()//figure.get_area()

class Square(Rectangle):

	def set_width(self, w):
		self.set_side(w)

	def set_height(self, h):
		self.set_side(h)

	def set_side(self, s):
		self.width = s
		self.height = s
		self.side = s

	def __init__(self, s):
		super().__init__(s,s)
		self.side = s

	def __str__(self):
		return f'Square(side={self.side})'		


print(Square(5))

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))
print(Rectangle(2,3).get_amount_inside(Rectangle(3, 6)))


# -----------------------------
# Conteúdo de arithmetic_formatter.py
# -----------------------------


#arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

#Output:

#Example Code
#  32         1      9999      523
#+  8    - 3801    + 9999    -  49
#----    ------    ------    -----
#  40     -3800     19998      474

#The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

#Situations that will return an error:
#If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
#The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. 
#Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
#Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
#Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'

#If the user supplied the correct format of problems, the conversion you return will follow these rules:
#There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, 
#both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
#Numbers should be right-aligned.
#There should be four spaces between each problem.
#There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

import operator
ops = { "+": operator.add, "-": operator.sub }

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    operands_one = []
    operands_two = []
    operators = []
    results = []
    dividers = []
    operands_two_oper = []

    for problem in problems:

        problem_parts = problem.split(' ')
        
        operand1 = problem_parts[0].strip()
        operator = problem_parts[1].strip()
        operand2 = problem_parts[2].strip()

        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        if not (operand1.isdigit() and operand2.isdigit()):            
            return 'Error: Numbers must only contain digits.'

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if len(operand1) < len(operand2):            
            divider = len(operand2) + 2 
        elif len(operand2) < len(operand1):
            divider = len(operand1) + 2
        else:
            divider = len(operand1) + 2

        operand1 = operand1.rjust(len('-'*divider))
        operand2 = operand2.rjust(len('-'*(divider-2)))

        operands_one.append(operand1)    
        operands_two.append(operand2)
        operators.append(operator)
        operands_two_oper.append((operator + ' ' + operand2))
        dividers.append('-'*divider)

        if show_answers:
            result = str(ops[operator](int(operand1),int(operand2)))
            result = result.rjust(len('-'*divider))
            results.append(result)


    problems = '    '.join(operands_one) + '\n' + '    '.join(operands_two_oper) + '\n' + '    '.join(dividers) 
    if show_answers:
        problems += '\n' + '    '.join(results)

    return problems

probls = ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]

print(f'\n{arithmetic_arranger(probls, False)}')


# -----------------------------
# Conteúdo de BinarySearchTree.py
# -----------------------------

#learn-tree-traversal-by-building-a-binary-search-tree
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-tree-traversal-by-building-a-binary-search-tree
#In this project, you are going to create a Binary Search Tree (BST). 
#A BST is a data structure in which each node has at most two children, with the left child containing values less than the parent node and the right child containing values greater than the parent node, allowing for efficient searching and sorting operations

class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

class BinarySearchTree:

    def __init__(self):
        #The root attribute represents the root node of the binary search tree. 
        #Since this is the constructor when a new BinarySearchTree object is created, it starts with an empty tree, so the root attribute is set to None
        self.root = None

    #Next, you need to define a mechanism to insert nodes in the tree. For that, you need to define an _insert method, which is a helper function and would be used by the actual insert method later on.
    #This method is recursive, meaning it calls itself to traverse the tree until the appropriate location for the new node is found.

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key) 
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left   
            
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)   
        
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)

print('Search for 80:', bst.search(80))

print("Inorder traversal:", bst.inorder_traversal())

bst.delete(40)

print("Search for 40:", bst.search(40))

print("Inorder traversal after deleting 40:", bst.inorder_traversal())

# -----------------------------
# Conteúdo de budget_app.py
# -----------------------------

#Build a Budget App Project
#Complete the Category class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. 
#When objects are created, they are passed in the name of the category. 
#The class should have an instance variable called ledger that is a list. 
#The class should also contain the following methods:

class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []

    #When the budget object is printed it should display:

    #A title line of 30 characters where the name of the category is centered in a line of * characters.
    #A list of the items in the ledger. Each line should show the description and amount. 
    #The first 23 characters of the description should be displayed, then the amount. 
    #The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    #A line displaying the category total.
    def __str__(self):
        str_print = f"{self.name.center(30, '*')}\n" 
        for entry in self.ledger:
            description = entry['description'][:23].ljust(23, ' ') 
            value = f"{entry['amount']:.2f}".rjust(7, ' ')
            str_print += f"{description}{value}\n"

        str_print += f"Total: {self.get_balance():.2f}"
        return(str_print)

    #1 - A deposit method that accepts an amount and description. 
    #If no description is given, it should default to an empty string. 
    #The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
    def deposit(self, amount, description=''):   
        self.ledger.append({'amount': amount, 'description': description})
    
    #2 - A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. 
    #If there are not enough funds, nothing should be added to the ledger. 
    #This method should return True if the withdrawal took place, and False otherwise.    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    #3 - A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    #4 - A transfer method that accepts an amount and another budget category as arguments. 
    #The method should add a withdrawal with the amount and the description 'Transfer to [Destination Budget Category]'. 
    #The method should then add a deposit to the other budget category with the amount and the description 'Transfer from [Source Budget Category]'. 
    #If there are not enough funds, nothing should be added to either ledgers. 
    #This method should return True if the transfer took place, and False otherwise.
    def transfer(self, amount, destination_category):
        if amount >= 0 and self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination_category.name}')
            destination_category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    #5 - A check_funds method that accepts an amount as an argument. 
    #It returns False if the amount is greater than the balance of the budget category and returns True otherwise. 
    #This method should be used by both the withdraw method and transfer method.
    def check_funds(self, amount):
        return self.get_balance() >= amount

#Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. 
#It should return a string that is a bar chart.
#The chart should show the percentage spent in each category passed in to the function. 
#The percentage spent should be calculated only with withdrawals and not with deposits. 
#Down the left side of the chart should be labels 0 - 100.
#The 'bars' in the bar chart should be made out of the 'o' character. 
#The height of each bar should be rounded down to the nearest 10. 
#The horizontal line below the bars should go two spaces past the final bar. 
#Each category name should be written vertically below the bar. There should be a title at the top that says 'Percentage spent by category'.

#This function will be tested with up to four categories.

#Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

#Percentage spent by category
#100|          
# 90|          
# 80|          
# 70|          
# 60| o        
# 50| o        
# 40| o        
# 30| o        
# 20| o  o     
# 10| o  o  o  
#  0| o  o  o  
#    ----------
#     F  C  A  
#     o  l  u  
#     o  o  t  
#     d  t  o  
#        h     
#        i     
#        n     
#        g     

def create_spend_chart(categories):
    graph = 'Percentage spent by category\n'


    # Calculate total spending and spending per category
    total_spent = sum(-item["amount"] for cat in categories for item in cat.ledger if item["amount"] < 0)
    category_spent = [(cat.name, sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)) for cat in categories]

    #print(category_spent)
    #print('total_spent', total_spent, '\n')

    # Compute spending percentages
    percentages = [(name, (spent / total_spent) * 100 if total_spent > 0 else 0) for name, spent in category_spent]
    #print(percentages)
    
    #imprimindo a parte de valores dos graficos
    for number in range(100,-10,-10):
        graph += f"{number}| ".rjust(5,' ')
        for _, percent in percentages:
            if percent >= number:
                graph += 'o' + 2 * ' '
            else:
                graph += 3 * ' '
        graph += '\n'

    graph += 4 * ' ' + ('-' * (len(category_spent)*3+1)) + '\n'


    #imprimindo as 'colunas' com os nomes das categorias
    #pegando a maior palavra
    #max([cat[0] for cat in category_spent], key=len)
    for i in range(max([len(cat.name) for cat in categories])):
        graph += 5 * ' '
        for cat in categories:
            if i < len(cat.name):
                graph += cat.name[i] + 2 * ' '
            else:
                graph += 3 * ' '

        graph += '\n'

    graph = graph.rstrip('\n')

    return graph    

#Here is an example usage:

    #food = Category('Food')
    #food.deposit(1000, 'deposit')
    #food.withdraw(10.15, 'groceries')
    #food.withdraw(15.89, 'restaurant and more food for dessert')
    #clothing = Category('Clothing')
    #food.transfer(50, clothing)
    #print(food)
    #And here is an example of the output:

    #*************Food*************
    #initial deposit        1000.00
    #groceries               -10.15
    #restaurant and more foo -15.89
    #Transfer to Clothing    -50.00
    #Total: 923.96

food = Category('Food')
clothing = Category('Clothing')
travel = Category('Travel')

food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

food.transfer(500, clothing)
travel.deposit(600, 'deposit')

clothing.withdraw(100, 'teste')
clothing.withdraw(50, 'teste1')

travel.withdraw(120, 'teste1')
travel.withdraw(80, 'teste1')

#print(clothing.ledger)
#print(food.ledger)
print(food, '\n')
#print(clothing, '\n')
#print(travel, '\n')

print(create_spend_chart([food, clothing, travel]))

# -----------------------------
# Conteúdo de caesar.py
# -----------------------------

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)

# -----------------------------
# Conteúdo de equation_solver.py
# -----------------------------

#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-interfaces-by-building-an-equation-solver
#learn-interfaces-by-building-an-equation-solver

#An interface is like a blueprint for a class. An interface contains a set of methods and properties that a class should implement.
#You want the LinearEquation class to implement and not simply inherit all the methods defined inside the Equation class, which should act as an interface.
#Currently, the Equation class is simply the parent class of LinearEquation. In the next steps you will learn how to turn it into a formal interface.
#ABC stands for Abstract Base Classes. The ABC class enables you to turn a regular class into an abstract class, which is a class that acts as a blueprint for concrete classes.
#Modify your import statement to import just the ABC class from the abc module. You can import a specific object x from a module y following the import construct from y import x.
#In order to be recognized as an abstract method, a method should be decorated with the @abstractmethod decorator.
#A decorator is used in Python to modify the behavior of a function. Here's an example of how to use a decorator named spam:
#	Example Code
#	@spam
#	def foo():
#    	pass
#In Python, data types are recognized during runtime (when the code is executed). 
#Therefore, you don't have to specify the data type of a variable when you declare it. 
#Nonetheless, you can annotate a variable to clarify that it will hold a specific data type with variable: <data type> = value or just variable: <data type>. 
#Note that the Python interpreter does not enforce the types used to annotate variables, and normally you'd need external tools to do it.

#The __init_subclass__ method is called whenever the class that defines it is subclassed and it enables to customize the child classes. 
#The method takes a parameter named by convention cls (standing for "class"), which represents the new child class.

#The hasattr built-in function takes an object as its first argument and a string representing an attribute name as its second argument. 
#It returns a boolean indicating if the object has the specified attribute.

#It's time to go back to the __init__ method. Depending on the equation type, you'll need to pass a variable number of arguments during the instantiation.
#Add a second parameter args to the method and use the * operator to make it accept a variable number of arguments.

#Each equation object will be instantiated passing as many arguments as the coefficients of the equation, starting from n-th degree of  x down to the zero-th degree, including the possible coefficient with the value of 0.
#For example, LinearEquation(4, 5) would represent the equation  4x+5=0, with 4 being the coefficient of the first (highest here) degree and 5 the coefficient of the zero-th degree.
#You need to check that the right number of arguments is passed to instantiate the equation object.

#The isinstance() built-in function takes two arguments and returns a Boolean indicating if the object passed as the first argument is an instance of the class passed as the second argument.
#Example Code
	#isinstance(7, int) # True


#The sub function from the re module enables you to replace text inside a string based on a regex pattern.

#Example Code
	#verse = 'Always look on the bright side of life'
	#spam = re.sub('bright', 'spam', verse)
	#spam == 'Always look on the spam side of life' # True

#It takes three arguments: the regex pattern to match, the replacement, and the string on which you want to perform the replacement.

#In a regex pattern, a lookaround is an assertion that matches a certain pattern without consuming characters in the string. 
#One kind of lookaround is the lookbehind, which can be either positive or negative. They are denoted by (?<=...) and (?<!...), respectively.
#Example Code
	#spam = 'black back bat'
	#re.sub('(?<=l)a', 'o', spam) == 'block back bat' # True
	#re.sub('(?<!l)a', 'o', spam) == 'black bock bot' # True

#In the example above, the pattern (?<=l)a contains a positive lookbehind, which is used to match the a character only when preceded by an l. 
#In the last line of the example, the pattern (?<!l)a contains a negative lookbehind, which is used to match the a character only if it is not preceded by an l. 
#Note how, in both cases, the character contained in the lookbehind is not consumed.

#Another kind of lookaround assertion is the lookahead. Positive and negative lookahead are denoted by (?=...) and (?!...), respectively. 
#They are used to match a pattern if followed by a certain sequence of characters, which is not consumed:

#Example Code
	#spam = 'black back bat'
	#re.sub('a(?=t)', 'o', spam) == 'black back bot' # True
	#re.sub('a(?!t)', 'o', spam) == 'block bock bat' # True
#In the example above, the pattern a(?=t) contains a positive lookahead, which is used to match the a character only when followed by a t. 
#In the last line of the example, the pattern a(?!t) contains a negative lookahead, which is used to match the a character only if not followed by a t. 
#Again, in both cases, the character contained in the lookahead is not consumed.


#An interesting feature of f-strings is the capability of forcing the output to be right/left-aligned, or centered. 
#After the expression to be evaluated is inside the curly braces, you need to write a colon followed by an alignment option (< to left-align, > to right-align, ^ to center) 
#and a number representing the width, that is the number of characters in which you want to arrange the text. 
#For example:
#Example Code
	#f'{"Hello World":>20}'
#Printing the string from the example above would result in right-aligned text arranged in a space of 20 characters
#Between the colon and the alignment option, you can specify a fill character, which will be used to fill the space around the text within the specified width
#Example Code (-)
	#f'{"Hello World":->20}'

#Another feature of f-strings enables you to convert the content of the replacement field (the curly braces) into a string by using a ! followed by the conversion type s. 
#For example, f'{obj!s}' converts obj into a string and it is equivalent to f'{str(obj)}'

#f-strings also enable you to set a specific precision to your numerical data by using the .nf format specifier, where n is the number of decimal digits to display.

#Within the curly braces of the f-strings contained inside result_list, write the format specifier needed to display 3 decimal digits just after the :+.

#The structural pattern matching enables you to verify that the subject has a specific structure. 
#In addition to that, it binds names in the pattern to elements of the subject. For example:
#Example Code
	#match my_list:
	#    case [a]:
	#        print(a)
	#    case [a, b]:
	#        print(a, b)

from abc import ABC, abstractmethod
import re

class Equation(ABC):
    degree: int
    type: str
  
    def __init__(self, *args):
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")

		#tanto o de cima qto esse de baixo funcionam
		#if not all([isinstance(arg, (int, float)) for arg in args]):
		#	raise TypeError("Coefficients must be of type 'int' or 'float'")

		#After validating the coefficients, you need to store them in an instance attribute. 
		#Use a dictionary comprehension to create a dictionary in which the key is the degree of the coefficient and the corresponding value is the coefficient, and assign it to an attribute named coefficients		
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    def __init_subclass__(cls):
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'type'"
            )            

    def __str__(self):
        terms = []
        for n, coefficient in self.coefficients.items():
            if not coefficient:
                continue
            if n == 0:
                terms.append(f'{coefficient:+}')
            elif n == 1:
                terms.append(f'{coefficient:+}x')
            else:
                terms.append(f"{coefficient:+}x**{n}")
        equation_string = ' '.join(terms) + ' = 0'
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))      
    
    @abstractmethod
    def solve(self):
        pass
        
    @abstractmethod
    def analyze(self):
        pass
        
class LinearEquation(Equation):
    degree = 1
    type = 'Linear Equation'
    
    def solve(self):
        a, b = self.coefficients.values()
        x = -b / a
        return [x]

    def analyze(self):
        slope, intercept = self.coefficients.values()
        return {'slope': slope, 'intercept': intercept}


class QuadraticEquation(Equation):
    degree = 2
    type = 'Quadratic Equation'

    def __init__(self, *args):
        super().__init__(*args)
        a, b, c = self.coefficients.values()
        self.delta = b**2 - 4 * a * c

    def solve(self):
        if self.delta < 0:
            return []
        a, b, _ = self.coefficients.values()
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)
        if self.delta == 0:
            return [x1]

        return [x1, x2]

    def analyze(self):
        a, b, c = self.coefficients.values()
        x = -b / (2 * a)
        y = a * x**2 + b * x + c
        if a > 0:
            concavity = 'upwards'
            min_max = 'min'
        else:
            concavity = 'downwards'
            min_max = 'max'
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}

def solver(equation):
    if not isinstance(equation, Equation):
        raise TypeError("Argument must be an Equation object")

    output_string = f'\n{equation.type:-^24}'
    output_string += f'\n\n{equation!s:^24}\n\n'
    output_string += f'{"Solutions":-^24}\n\n'
    results = equation.solve()
    match results:
        case []:
            result_list = ['No real roots']
        case [x]:
            result_list = [f'x = {x:+.3f}']
        case [x1, x2]:
            result_list = [f'x1 = {x1:+.3f}', f'x2 = {x2:+.3f}']
    for result in result_list:
        output_string += f'{result:^24}\n'
    output_string += f'\n{"Details":-^24}\n\n'
    details = equation.analyze()
    match details:
        case {'slope': slope, 'intercept': intercept}:
            details_list = [f'slope = {slope:>16.3f}', f'y-intercept = {intercept:>10.3f}']
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:
            coord = f'({x:.3f}, {y:.3f})'
            details_list = [f'concavity = {concavity:>12}', f'{min_max} = {coord:>18}']
    for detail in details_list:
        output_string += f'{detail}\n'
    return output_string

lin_eq = LinearEquation(2, 3)
quadr_eq = QuadraticEquation(1, 2, 1)
print(solver(quadr_eq))

# -----------------------------
# Conteúdo de generate_password.py
# -----------------------------

#learn-regular-expressions-by-building-a-password-generator
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-regular-expressions-by-building-a-password-generator
import re
import secrets
import string

#The caret, ^, placed at the beginning of the character class, matches all the characters except those specified in the class.
#The dot character is a wildcard that matches any character in a string — except for a newline character by default. Modify pattern to match the entire string by replacing the current pattern with a . followed by the + quantifier.
#If you need to match a character that has a special meaning in the pattern, such as . or +, you can escape it by prepending a backslash character, \. For example, this matches a literal plus sign: \+.
#Python provides a particular type of string called raw string. Raw strings are prefixed with a r. 
#The key distinction from regular strings lies in how they handle the backslash character: in raw strings, backslashes are treated as literal characters rather than escape characters. 
#When writing regular expressions, using raw strings is a good practice, since they can usually contain a lot of \ characters.

def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
       
        #The character class \d is a shorthand for [0-9]. Replace this character class with the shorthand inside your first constraint tuple.
        #In a character class, you can combine multiple ranges by writing one range after another inside the square brackets (without any additional characters). 
        #For example: [a-d3-6] is the combination of [a-d] and [3-6].
        #Now, modify the last regex pattern to match any non-alphanumeric character. 
        #Combine the a-z, A-Z, and 0-9 ranges into a single character class and add a ^ as the first character to negate the pattern.        
        #In the same way the [0-9] class is equivalent to \d, the [^0-9] class is equivalent to \D. 
        #Alphanumeric characters can be matched with \w and non-alphanumeric characters can be matched with \W.
        #Replace the [^a-zA-Z0-9] character class with \W
        #Since the underscore character is a valid character for variable names, it is included in the \w character class (equivalent to [a-zA-Z0-9_]), which can be conveniently used to match variable names.
        #Therefore, the \W character class is equivalent to [^a-zA-Z0-9_] with the underscore character that is not matched. For this reason you cannot use it to match all your special characters.        
        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),            
            (special_chars, fr'[{symbols}]')            
        ]

        # Check constraints
        count = 0
        for constraint, pattern in constraints:
            if constraint <= len(re.findall(pattern, password)):
                count += 1
            
        if count == 4:
            break

    return password

def generate_password2(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
   
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    constraints = [
        (nums, r'\d'),
        (special_chars, fr'[{symbols}]'),
        (uppercase, r'[A-Z]'),
        (lowercase, r'[a-z]')
    ]

    #print(constraints)
    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        
        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
        #print(password)
    return password

#isso faz com que essa parte do código seja executada somente quando o arquivo generated_passorwd.py for chamado
#se ele for importado para dentro de outro programa o codigo abaixo não será executado
#essa construção é bastante interessante pq vc pode escrever codigos de teste dentro do seu próprio módulo (arquivo) e eles serão executados somente quando o arquivo for executado python3 generated_passorwd.py
if __name__ == '__main__':
    new_password = generate_password2(8, 2, 1, 1, 1)
    print(new_password)

# -----------------------------
# Conteúdo de lambda.py
# -----------------------------

#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-lambda-functions-by-building-an-expense-tracker
#learn-lambda-functions-by-building-an-expense-tracker

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
#Lambda functions are brief, anonymous functions in Python, ideal for simple, one-time tasks. 
#They are defined by the lambda keyword, and they use the following syntax:
#lambda x: expr
#In the example above, x represents a parameter to be used in the expression expr, and it acts just like any parameter in a traditional function. 
#expr is the expression that gets evaluated and returned when the lambda function is called.
#Lambda functions can be valuably combined with the map() function, which executes a specified function for each element in a collection of objects, such as a list:
#map(lambda x: x * 2, [1, 2, 3])
#The function to execute is passed as the first argument, and the iterable is passed as the second argument.
#The result of the example above would be [2, 4, 6], where each item in the list passed to map() has been doubled by the action of the lambda function.
#The sum() function returns the sum of the items in the iterable which is passed as its argument. You are going to use sum() together with map() and lambda functions to get the total amount of expenses.

def total_expenses(expenses):
    #create lambda function that has expense as its parameter.
    #expense is expected to be a dictionary, and your lambda function should return the value of the 'amount' key in the expense dictionary.
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    #Use expense as the parameter and evaluate the comparison between the value of the 'category' key of the expense dictionary and category using the equality operator.
    #The filter() function allows you to select items from an iterable, such as a list, based on the output of a function:
    #filter(my_function, my_list)
    #filter() takes a function as its first argument and an iterable as its second argument. It returns an iterator, which is a special object that enables you to iterate over the elements of a collection, like a list.
    #The result of the example above is an iterator containing the elements of my_list for which my_function returns True    
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break
main()

# -----------------------------
# Conteúdo de List_Comprehension.py
# -----------------------------

#learn-list-comprehension-by-building-a-case-converter-program
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-list-comprehension-by-building-a-case-converter-program
#In this project, you are going to build a program that takes a camelCase or PascalCase formatted string as input and converts that to a snake_case formatted string using two approaches. 
#First, you'll use a for loop and then list comprehension to achieve the same results. You'll see how list comprehension can make your code more concise.
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string

def convert_to_snake_case_list_comprehension(pascal_or_camel_cased_string):
    #in Python, a list comprehension is a construct that allows you to generate a new list by applying an expression to each item in an existing iterable and optionally filtering items with a condition. 
    #Apart from being briefer, list comprehensions often run faster.
    #A basic list comprehension consists of an expression followed by a for clause:
    #spam = [i * 2 for i in iterable]
    #The above uses the variable i to iterate over iterable. Each elements of the resulting list is obtained by evaluating the expression i * 2 at the current iteration.    

    #quando só tem o if sem o else a construção muda
    #snake_cased_char_list = ['_' + char.lower() for char in pascal_or_camel_cased_string if char.isupper()]
    snake_cased_char_list = ['_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()


# -----------------------------
# Conteúdo de lunh.py
# -----------------------------

#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-how-to-work-with-numbers-and-strings-by-implementing-the-luhn-algorithm
#learn-how-to-work-with-numbers-and-strings-by-implementing-the-luhn-algorithm
#Here's a step-by-step explanation of how the Luhn algorithm works:

#Starting from the rightmost digit (the check digit), move left and double the value of every second digit.
#If doubling a digit results in a number greater than 9, subtract 9 from the result.
#Sum all the digits (both the doubled and the untouched ones).
#If the total modulo 10 is equal to 0 (i.e., the total ends in zero), then the number is valid according to the Luhn formula.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            #Part of the algorithm is to double every second digit, starting from the right. 
            #If the result of doubling the number is greater than or equal to 10, add the two digits together. 
            #For example, if the digit is 6, double it to get 12. Add 1 and 2 together to get 3. 
            #You can do this by using integer division to get the first digit and the modulus operator (%) to get the second digit:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    #Python comes with built-in classes that can help us with string manipulation. One of them is the str class. 
    #It has a method called maketrans that can help us create a translation table. This table can be used to replace characters in a string:
    #str.maketrans({'t': 'c', 'l': 'b'})
    #The above, when called on a string, will replace all t characters with c and all l characters with b.    
    card_translation = str.maketrans({'-': '', ' ': ''})
    #Defining the translation does not in itself translate the string. The translate method must be called on the string to be translated with the translation table as an argument:
    #my_string = "tamperlot"
    #translation_table = str.maketrans({'t': 'c', 'l': 'b'})
    #translated_string = my_string.translate(translation_table)    
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()

# -----------------------------
# Conteúdo de merge_sort.py
# -----------------------------

#learn-data-structures-by-building-the-merge-sort-algorithm
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-data-structures-by-building-the-merge-sort-algorithm
#In this project, you willl learn data structures by building the merge sort algorithm.

#This is a sorting algorithm that uses the divide-and-conquer principle to sort collections of data. 
#That is, it 'divides' a collection into smaller sub-parts, and 'conquers' the sub-parts by sorting them independently, then merges the sorted sub-parts.
#The merge sort algorithm mainly performs three actions:

#Divide an unsorted sequence of items into sub-parts
#Sort the items in the sub-parts
#Merge the sorted sub-parts
#The above happens recursively until the sub-parts are merged into the complete sorted sequence. Let's start by dividing the sequence.
#The merge sort algorithm mainly performs three actions:
    #Divide an unsorted sequence of items into sub-parts
    #Sort the items in the sub-parts
    #Merge the sorted sub-parts
#The above happens recursively until the sub-parts are merged into the complete sorted sequence. 
#Let's start by dividing the sequence.

def merge_sort(array):
    #Before testing the merge_sort() function, you need to create a base case that stops the function execution when the length of array is less than or equal to 1.
    #This base case will stop the recursion call. Without it, the merge sort operation would continue to run even when the list has been sorted or has no element in it.
    #Right after the function declaration, create an if statement with this condition: len(array) <= 1. Use the pass keyword in the function's body.    
    if len(array) <= 1:
        return
    
    #print('array', array)
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    #print('left_part', left_part)
    #print('right_part', right_part)

    #print('____________________________')

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    #Inside your function, create a while loop that compares an element in left_part to an element in right_part, and merges the smaller element to the main array list.
    #Create two conditions for the loop: one that checks whether the left_array_index is less than the length of left_part and another condition that checks whether right_array_index is less than the length of right_part.    

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        #if statement that checks if the index of left_part is less than the index of right_part.
        #When the if condition evaluates to True, it means that the element in the left_part list is smaller than the element it is being compared to in the right_part list.
        #In that case, you can assign the left_part index to the sorted array.        
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    #The while loop you created compares one element from left_part with another in right_part, then adds the smaller element to the main array list.
    #It will continue this operation until there are no elements left to be compared. But left_part may still have elements left while right_part has none, and vice versa.
    #Create another while loop to copy the remaining elements in left_part into the array list. Use left_array_index < len(left_part) for the while condition.        

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1
    
    #print('array sorted', array)

#You can use the __name__ variable to determine if a Python script is being run as the main program or if it is being imported as a module (code written in another Python file).
#If the value of __name__ is set to '__main__', it implies that the current script is the main program, and not a module.
#In this project, you'll use the current script as the main program.

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))



# -----------------------------
# Conteúdo de probability_calculator.py
# -----------------------------

#Build a Probability Calculator Project
#Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. 
# What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? 
# While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

#For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

#First, create a Hat class in main.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:

#hat1 = Hat(yellow=3, blue=2, green=6)
#hat2 = Hat(red=5, orange=4)
#hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
#A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be a list of strings containing one item for each ball in the hat.
#Each item in the list should be a color name representing a single ball of that color. For example, if your hat is {'red': 2, 'blue': 1}, contents should be ['red', 'red', 'blue'].

#The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. 
# This method should remove balls at random from contents and return those balls as a list of strings. 
# The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. 
# If the number of balls to draw exceeds the available quantity, return all the balls.

#Next, create an experiment function in main.py (not inside the Hat class). This function should accept the following arguments:

#hat: A hat object containing balls that should be copied inside the function.
#expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. ,
#   For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {'blue':2, 'red':1}.
#num_balls_drawn: The number of balls to draw out of the hat in each experiment.
#num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

#The experiment function should return a probability.

#For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. 
# To do this, you will perform N experiments, count how many times M you get at least two red balls and one green ball, and estimate the probability as M/N. 
# Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.

#Here is how you would call the experiment function based on the example above with 2000 experiments:

#hat = Hat(black=6, red=4, green=3)
#probability = experiment(hat=hat,
#                  expected_balls={'red':2,'green':1},
#                  num_balls_drawn=5,
#                  num_experiments=2000)
#The output would be something like this:

#0.356
#Since this is based on random draws, the probability will be slightly different each time the code is run.

#Hint: Consider using the modules that are already imported at the top. Do not initialize random seed within the file.

import copy
import random

class Hat:
    def __init__(self, **kwargs):
        if not kwargs:  # Verifica se nenhum argumento foi passado
            raise ValueError("É necessário fornecer pelo menos um argumento.")

        self.contents = []
        for key, value in kwargs.items():
            self.contents += [key] * value

    def draw(self, number_of_balls):        
        draw_list = []

        if number_of_balls >= len(self.contents):
            number_of_balls = len(self.contents)
        
        for _ in range(number_of_balls):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            draw_list.append(ball)

        return draw_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    if sum(expected_balls.values()) > num_balls_drawn:
        raise ValueError("É necessário fornecer um número de bolas maior.")
    
    hat_exp = copy.deepcopy(hat)
    for _ in range(num_experiments):
        draw_list = hat_exp.draw(num_balls_drawn)
        draw_dict = {}
        
        for ball in draw_list:
            draw_dict[ball] = draw_dict.get(ball, 0) + 1
        
        inclusive = expected_balls.keys() <= draw_dict.keys()
        if  inclusive:
            for key in expected_balls.keys():
                if draw_dict[key] < expected_balls[key]:
                    inclusive = False
        if inclusive:
            M += 1
        hat_exp = copy.deepcopy(hat)
    return M / num_experiments        


#d1 = {'red': 2, 'green': 1}
#d2 = {'red': 2, 'green': 3, 'blue': 1}
#contido = d1.keys() <= d2.keys()
#print(contido)

#teste = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
#print(teste.contents)
#print(teste.draw(3)) 
#print(teste.contents)   

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)

# -----------------------------
# Conteúdo de projectile_trajectory_calculator.py
# -----------------------------

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

# -----------------------------
# Conteúdo de shortest_path.py
# -----------------------------


#learn-algorithm-design-by-building-a-shortest-path-algorithm
#https://github.com/freeCodeCamp/freeCodeCamp/blob/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-algorithm-design-by-building-a-shortest-path-algorithm/65576ff7888f9e96f52a4be1.md

#A graph is called a weighted graph when its edges are associated with weights, representing a distance, time or other quantitative value.
#In your case, these weights will be the distances between each node, or point in space. To represent a weighted graph you can modify your dictionary, using a list of tuples for each value.
#The first element in the tuple will be the connected node, and the second element will be an integer number indicating the distance.
#Modify my_graph['A'] into a list of tuples, considering that the A-B distance is 3 and the A-D distance is 1.
#The algorithm will start at a specified node. Then it will explore the graph to find the shortest path between the starting node, or source, and all the other nodes.
#For that your function needs two parameters: graph, and start. Add them to your function declaration.
#To keep track of the visited nodes, you need a list of all the nodes in the graph. Once a node is visited, it will be removed from that list.
#Now, replace the pass keyword with a variable named unvisited and assign it an empty list.
#Create a for loop to iterate over your graph, and use the .append() method to add each node to the end of the unvisited list.
#While the algorithm explores the graph, it should keep track of the currently known shortest distance between the starting node and the other nodes.
#Before your for loop, create a new variable named distances and assign it an empty dictionary.
#The distance from the starting node is zero, because the algorithm begins its assessment right from there.
#After appending node to unvisited in your loop, create an if statement that triggers if the node is equal to the starting node. 
#Then assign 0 to that node inside the distances dictionary.
#At the beginning, all the other nodes in the graph are considered to be at infinite distance from the source node, because the distance has not been determined yet.
#Create an else clause and assign an infinite value to the node in the distances dictionary. 
#For that, use the float() function with the string 'inf' as argument to generate a floating point number representing the positive infinity.
#After your for loop, add a print() call and pass in the following string to see the values of the variables you have created: f'Unvisited: {unvisited}\nDistances: {distances}'.
#All the distances in distances are set to infinite, except for the starting node. 
#The unvisited list contains all the nodes in your graph. But actually, you don't need that for loop to achieve this result.
#Remove your for loop with its entire body. --> aqui eu criei outra função



my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path_old(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    print(f'Unvisited: {unvisited}\nDistances: {distances}')

#Your function is going to explore all the nodes connected to the starting node. It will calculate the shortest paths for all of them. 
#Then, it will remove the starting node from the unvisited nodes.
#Next, the closest neighbor node will be visited and the process will be repeated until all the nodes are visited.    
def shortest_path(graph, start, target=''):
    #The list() type constructor enables you to build a list from an iterable.
    #Modify the assignment of your unvisited variable to use list(), and pass graph as the iterable.
    unvisited = list(graph)
    distances = {}    

    #With a dictionary comprehension, you can create a dictionary starting from an existing dictionary:
    #{key: val for key in dict}
    #In the example above, val is the value that key will have in the new dictionary, and dict is the existing dictionary.
    #You want to keep track of the paths between the starting node and each other node.
    #After the distances variable, create a paths variable and assign it a dictionary with all the keys from graph. 
    #Assign an empty list to each key and use a dictionary comprehension to build your dictionary.
    
    paths = {node: [] for node in graph}

    #Dictionary comprehensions support conditional if/else syntax too:
    #{key: val_1 if condition else val_2 for key in dict}
    #In the example above, dict is the existing dictionary. 
    #When condition evaluates to True, key will have the value val_1 , otherwise val_2.
    #Use a dictionary comprehension to create a dictionary based on graph and assign it to the distances variable. 
    #Give the key a value of zero if the node is equal to the starting node, and infinite otherwise. Use float('inf') to achieve the latter.
    distances = {node: 0 if node == start else float('inf') for node in graph}

    #Since the algorithm begins its assessment from the starting node, after creating the paths dictionary, you need to add the starting node to its own list in the paths dictionary.
    #Use the .append() method to append start to the paths[start] list.
    paths[start].append(start)

    #min() takes also a keyword-only argument. 
    #Passing a function as an additional argument to min(), you can modify the way the list items are compared.
    #The result of the line you've just written in the previous step is the node that comes first in alphabetical order. 
    #Instead you want to select the unvisited node having the smallest distance from the starting node.
    #Pass key=distances.get as the second argument to your min() call. 
    #In this way, the comparison will take place depending on the value each unvisited list item has inside the distances dictionary.    

    print(f'\nGraph: {graph}\nUnvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}\n')

    #Inside the while loop, the first thing to do is define the current node to visit. 
    #For that you can use the min() function. It returns the smallest item from the iterable passed as the argument.
    #Remove pass, then create a variable called current and assign it min(unvisited).
    #min() takes also a keyword-only argument. Passing a function as an additional argument to min(), you can modify the way the list items are compared.
    #The result of the line you've just written in the previous step is the node that comes first in alphabetical order. 
    #Instead you want to select the unvisited node having the smallest distance from the starting node.
    #Pass key=distances.get as the second argument to your min() call. 
    #In this way, the comparison will take place depending on the value each unvisited list item has inside the distances dictionary.

    while unvisited:
        current = min(unvisited, key=distances.get)
        print('current', current)
        print(f'graph no node current[{current}]', graph[current])

        for node, distance in graph[current]:
            print('node', node)
            print('distance', distance)
            print(f'distances no node [{node}]', distances[node])
            print(f'distances em current[{current}]', distances[current])

            #Create an if statement to check if the distance of the neighbor node (the second item in the processed tuple) plus the distance of current is less than the currently known distance of the neighbor node (the first item in the processed tuple).
            #Once the distance to a node is set inside the distances dictionary, you need to keep track of the path to that node, too. 
            #If the distance for the node in the processed tuple has been updated, the last item in its path is the node itself.
            #Inside your conditional, nest another if statement that triggers when the last element of paths[node] is equal to node.

            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                print(f'nova distances no node [{node}]', distances[node])
                print('\npaths', paths)
                print(f'paths no node [{node}]', paths[node])
                print(f'paths de current[{current}]', paths[current])
                if paths[node] and paths[node][-1] == node:
                    print(f'paths no node [{node}][-1]', paths[node][-1])
                    #When a shorter distance is found for a neighbor node, paths[current] gets assigned to the neighbor node path, paths[node].
                    #This means both variables point to the same list. Since lists are mutable, when you append the neighbor node to its path, both paths[node] and paths[current] are modified because they are the same list. 
                    #This results in wrong paths, although the distances are correct.
                    #You can fix that bug by assigning a copy of paths[current] to the neighbor node path.                    
                    paths[node] = paths[current][:]
                else:
                    #The .extend() method, allows you to add elements from an iterable to the end of a list:
                    #Example Code
                    #my_list = ['larch', 'birch']
                    #tree_list = ['fir', 'redwood', 'pine']
                    #my_list.extend(tree_list)
                    #print(my_list) # Output: ['larch', 'birch', 'fir', 'redwood', 'pine']                    
                    paths[node].extend(paths[current])

                print(f'paths novo node [{node}]', paths[node])
                paths[node].append(node)
                print('______\n')

        #The .remove() method removes from a list the first matching element that is passed as the argument:
        unvisited.remove(current)
        print('+++++++++\n')
    print(f'Graph: {graph}\nUnvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}\n')


def shortest_path_new(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    #Python provides a concise way to write if/else conditionals by using the ternary syntax:
    #val_1 if condition else val_2
    #The expression above evaluates to val_1 if condition is true, otherwise to val_2.    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths

shortest_path(my_graph, 'A')

# -----------------------------
# Conteúdo de square_root_bisection.py
# -----------------------------

#learn-the-bisection-method-by-finding-the-square-root-of-a-numbe
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-the-bisection-method-by-finding-the-square-root-of-a-number
#In this project, you will find the approximate square root of a given number using the bisection method.
#The bisection method is a technique for finding the roots of a real-valued function. 
#It works by narrowing down an interval where the square root lies until it converges to a value within a specified tolerance.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            #print('low', low, 'high', high, 'mid', mid, 'root', root, 'square_mid', square_mid)

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

valor = float(input('digite um numero:'))
print('raiz', square_root_bisection(valor))

# -----------------------------
# Conteúdo de sudoku.py
# -----------------------------

#learn-classes-and-objects-by-building-a-sudoku-solver/
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-classes-and-objects-by-building-a-sudoku-solver

#A generator expression in Python is a concise way to create a generator without the need for a full generator function. 
#It allows you to generate values on the fly and is often used for memory-efficient iteration over large datasets. 
#Generator expressions are similar to list comprehensions but use parentheses instead of square brackets.
#Here's a simple example to illustrate:
### ---List comprehension
#squares_list = [x**2 for x in range(10)]
#print(squares_list)
### Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

###---Generator expression
#squares_gen = (x**2 for x in range(10))
#print(squares_gen)
#### Output: <generator object <genexpr> at 0x...>

### To get the values from the generator, you can use a loop or convert it to a list
#for square in squares_gen:
#    print(square)
### Output: 0 1 4 9 16 25 36 49 64 81

class Board:
    #The instantiation creates an empty object. The __init__ method is a special method that allows you to instantiate an object to a customized state. 
    #When a class implements an __init__ method, __init__ is automatically called upon instantiation.
    #Inside your Board class, delete the spam method and replace it with an __init__ method that includes a self parameter.    
    def __init__(self, board):
        self.board = board

    #The __str__ method is a special method that is called under the hood when the object is printed using the print() function, 
    #or converted into a string using the str() function.
    def __str__(self):
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str    

    def find_empty_cell(self):
        #The enumerate built-in function takes an iterable as its argument and returns an enumerate object you can iterate over. 
        #It provides the count (which by default starts at zero) and the value from the iterable.
        #iterable = ['a', 'b', 'c']
        #for i, j in enumerate(iterable):
        #    print(i, j)
        #The loop from the example above would output the tuples 0, a, 1, b, and 2, c.
        #Inside the find_empty_cell method, replace pass with a for loop that uses the enumerate() function to iterate over each row in the sudoku board. 
        #Use row as the index of the current row and contents for the elements of the current row
        for row, contents in enumerate(self.board):
            print(row, contents)
            #The .index() method raises a ValueError exception when the value is not found. 
            #To prevent the program from halting execution, you'll nest this line of code inside a try block. 
            #The try statement is used to encapsulate code that might raise an exception. 
            #The except clause, on the other hand, offers alternative code to execute if an exception occurs:
            try:
                col = contents.index(20)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]   

    def valid_in_col(self, col, num):

        #generator expression
        #generator nesse caso vai gerar uma lista de booleans
        #all function vai verificar se todos os resultados dessa função são verdadeiros
        all((self.board[row][col] != num for row in range(9)))

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        #print(f'row given is {row} and col given is {col} row_start is {row_start} and col_start is {col_start}')
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                #print(f'row, col [{row_no}, {col_no}]')
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        #A tuple can be unpacked, meaning that the elements contained in the tuple can be assigned to variables, like this:
        #spam = ('lemon', 'curry')
        #item1, item2 = spam
        #In the example above, item1 would have the value 'lemon' and item2 would have the value 'curry'.        
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        #The generator expression you just wrote in the previous step generates a list of boolean values representing whether the condition self.board[row][col] != num is True or False for each element in the specified column across all rows.
        #Pass that generator expression to the all() function to check if all the elements in the column are different from num and return the result.        
        return all([valid_in_row, valid_in_col, valid_in_square])

    #The := operator gives you the ability to assign variables in the middle of an expression. 
    #The syntax is: name := val, where name is the variable name and val is the variable value.
    #This construct is formally named assignment expressions, 
    #while the := operator is commonly referred to as the walrus operator.        
    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False

def solve_sudoku(board):
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')

    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    
    return gameboard

puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)

# -----------------------------
# Conteúdo de time_calculator.py
# -----------------------------


#Write a function named add_time that takes in two required parameters and one optional parameter:

#a start time in the 12-hour clock format (ending in AM or PM)
#a duration time that indicates the number of hours and minutes
#(optional) a starting day of the week, case insensitive
#The function should add the duration time to the start time and return the result.

#If the result will be the next day, it should show (next day) after the time. 
#If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

#If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. 
#The day of the week in the output should appear after the time and before the number of days later.

def add_time(start, duration, day_of_the_week=''):
    #hour_start = int(start.split(':')[0])
    #min_start = int(start.split(':')[1].split(' ')[0])
    #start_period = start.split(':')[1].split(' ')[1]

    # Parsing start time
    start_hour, rest = start.split(':')
    start_min, start_period = rest.split(' ')
    start_hour, start_min = int(start_hour), int(start_min)

    # Parsing duration
    duration_hour, duration_min = map(int, duration.split(':'))
    #hour_duration = int(duration.split(':')[0])
    #min_duration = int(duration.split(':')[1])

    new_hour = start_hour + duration_hour
    new_min = start_min + duration_min

    #print ('1', 'new_hour', new_hour, 'new_min', new_min, 'start_period', start_period)

    if new_min >= 60:
        new_hour += 1
        new_min -= 60
    
    number_of_days = new_hour // 24
    new_hour = new_hour % 24

    #print ('2', 'new_hour', new_hour, 'new_min', new_min, 'start_period', start_period, 'number_of_days', number_of_days)

    if new_hour >= 12:
        if new_hour > 12:
            new_hour -= 12
        if start_period == 'AM':
            start_period = 'PM'
        else:
            start_period = 'AM'
            number_of_days += 1
    
    #print ('3', 'new_hour', new_hour, 'new_min', new_min, 'start_period', start_period, 'number_of_days', number_of_days)

    
    if number_of_days > 1:
        per = f'({number_of_days} days later)'
    elif number_of_days == 1:
        per = '(next day)'
    else:
        per = ''
    
    new_min = str(new_min).rjust(2,'0')

    new_day = ''
    if day_of_the_week:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        index = (days_of_week.index(day_of_the_week.capitalize()) + number_of_days) % 7
        new_day = f', {days_of_week[index]}'

    new_time = f'{new_hour}:{new_min} {start_period}{new_day} {per}'
    
    #print ('new_hour', new_hour, 'new_min', new_min, 'start_period', start_period, 'number_of_days', number_of_days)
    return new_time

print('3:30 PM', '2:12')
print(add_time('3:30 PM', '2:12'), '\n')

print('11:55 AM', '3:12')
print(add_time('11:55 AM', '3:12'), '\n')

print('2:59 AM', '24:00')
print(add_time('2:59 AM', '24:00'), '\n')

print('8:16 PM', '466:02')
print(add_time('8:16 PM', '466:02'), '\n')

print('3:30 PM', '2:12', 'Monday')
print(add_time('3:30 PM', '2:12', 'Monday'), '\n')

print('11:59 PM', '24:05', 'Wednesday')
print(add_time('11:59 PM', '24:05', 'Wednesday'),'\n')

print('2:59 AM', '24:00', 'saturDay')
print(add_time('2:59 AM', '24:00', 'saturDay'), '\n')

print('8:16 PM', '466:02', 'tuesday')
print(add_time('8:16 PM', '466:02', 'tuesday'))

# -----------------------------
# Conteúdo de tower_of_hanoy_recursion.py
# -----------------------------

#learn-recursion-by-solving-the-tower-of-hanoi-puzzle
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-recursion-by-solving-the-tower-of-hanoi-puzzle
#The goal of the Tower of Hanoi is moving all the disks to the last rod. 
#To do that, you must follow three simple rules:

#You can move only top-most disks
#You can move only one disk at a time
#You cannot place larger disks on top of smaller ones

#In the Tower of Hanoi puzzle, you can identify the three rods according to their purpose:

#The first rod is the source, where all the disks are stacked on top of each other at the beginning of the game.
#The second rod is an auxiliary rod, and it helps in moving the disks to the target rod.
#The third rod is the target, where all the disks should be placed in order at the end of the game.

NUMBER_OF_DISKS = 5
#The Tower of Hanoi puzzle can be solved in 2n - 1 moves, where n is the number of disks.
number_of_moves = 2**NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def make_allowed_move(rod1, rod2):    
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True      
                
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    
    # display our progress
    print(rods, '\n')

def move(n, source, auxiliary, target):
    # display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)     

# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')

print('_________now the recursion__________')

A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move_rec(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    
    # move the nth disk from source to target
    target.append(source.pop())
    
    # display our progress
    print(A, B, C, '\n')
    
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move_rec(NUMBER_OF_DISKS, A, B, C)

# -----------------------------
# Conteúdo de vector_space.py
# -----------------------------

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

# -----------------------------
# Conteúdo de vigenere.py
# -----------------------------

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)
    
encryption = encrypt(text, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)

