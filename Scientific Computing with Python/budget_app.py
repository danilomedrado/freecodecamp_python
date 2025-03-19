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