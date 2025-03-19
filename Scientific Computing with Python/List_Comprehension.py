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
