import re

file = open('regex_sum_2166897.txt')

text_file = file.read()

numbers = re.findall('[0-9]+', text_file)

print(sum([int(number) for number in numbers]))