
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
