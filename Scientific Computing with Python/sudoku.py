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