import re

def onlydigit(Teststring):
    pattern = '\d+'
    result = re.findall(pattern, Teststring)
    return result


print("Enter the test string for match")
input_string = 'There are 4 boxes , 5 pencils, 33 windoes.'
numbers = onlydigit(input_string)
print(numbers)