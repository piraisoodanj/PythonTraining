# Create a function that return if the number is odd or even. you should call this function for both usecases(odd/even)

def oddeven(number):
    if(number%2==0):
        return "even"
    else:
        return "odd"


#print(oddeven(4))

print("Enter the number")
user_input= input()
print(oddeven(int(user_input)))
