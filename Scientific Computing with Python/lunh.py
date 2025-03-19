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