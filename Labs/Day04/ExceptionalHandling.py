try:
    num1= int(input())
    num2= int(input())
    result = num1/num2
    print(result)

except ZeroDivisionError as e:
    print("you cannot divide by o")

print("finally statment executed")