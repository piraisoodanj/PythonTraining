import re

def onlydigit(Teststring):
    pattern = r'\bs\w*'
    result = re.findall(pattern, Teststring,re.IGNORECASE)
    return result


print("Enter the test string for match")
input_string = input()
numbers = onlydigit(input_string)
print(numbers)