import re

def FindDate(Teststring):
    pattern = '\d{4}[-/]\d{2}[-/]\d{2}'
    result = re.findall(pattern, Teststring,re.IGNORECASE)
    return result


#print("Enter the test string for match")
input_string = 'I have work on 2024-02-02 and also on 2024/03/08'
numbers = FindDate(input_string)
print(numbers)