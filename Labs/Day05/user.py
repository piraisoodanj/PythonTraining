# create a program to get a value from user and keep loop running until it exit

def arithmeticOp(a, b , Opera):
    if(Opera=='Add'):
        return a+b
    elif(Opera=='Sub'):
        return a-b
    elif(Opera=='Mul'):
        return a*b
    elif(Opera=='Divide'):
        return a//b


choice = ""
while choice!="exit":
    print("1. Add Two Numbers")
    print("2. Subtract Two Numbers")
    print("3. Divide Two Numbers")
    print("4. Multiply Two Numbers")
    print("5. Exit")
    number = int(input())
    if(number == 1):
       print("Enter First Number")
       number1= int(input())
       print("Enter Second Number")
       number2=int(input())
       Add= number1+number2
       print("Adding Two Number", arithmeticOp(number1, number2 , 'Add'))
    elif(number == 2):
        print("Enter First Number")
        number3 =int(input())
        print("Enter Second Number")
        number4=int(input())
        print("Subtract Two Number", arithmeticOp(number3, number4 , 'Sub'))
    elif(number == 3):
        print("Enter First Number")
        number3 =int(input())
        print("Enter Second Number")
        number4=int(input())
        print("Divide Two Number", arithmeticOp(number3, number4 , 'Divide'))
    elif(number == 4):
        print("Enter First Number")

        number3 =int(input())
        print("Enter Second Number")
        number4=int(input())
        print("Multiply Two Number",arithmeticOp(number3, number4 , 'Mul'))
    elif(number == 5):
        choice = "exit"

    
    

