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