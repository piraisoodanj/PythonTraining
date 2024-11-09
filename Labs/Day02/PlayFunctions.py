def say_hello(name):
    return "Hello " + name
print(say_hello("Pirai"))


def thirdchar(name, n):
    return name[n-1::n]

print(thirdchar("Pirai",3))

def reverseString(name):
    return name[len(name)-1::-1]
   # return name[::-1]

print(reverseString("pirai"))