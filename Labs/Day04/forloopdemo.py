def loop(num,name):
    '''Function for printing num and name with help of number range'''
    for i in range(num):
        print(i)
        print(name)

'''Enter the number for looping'''
num = int(input())
'''Enter the username for display'''
name = input()
loop(num,name)

