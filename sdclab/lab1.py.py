"""n=int(input("enter the number:"))
print(n)
if n%2==0:
    print("the number is even")
else:
    print("the number is odd")"""
#_____________________________
"""sum = 0
s = input("\nenter an integer value: ")
n = int(s)
while n != 0:
    sum = sum + n
    s = input("enter an integer value: ")
    n = int(s)

print("sum of given value is:", sum)
"""
#________________________________
"""isprime=True
i=2
n=int(input("enter a number:"))
while i<n:
    reminder=n%i
    if reminder==0:
        isprime=False 
        break
    else:
        i=i+1
if isprime:
    print("number is prime")
else:
    print("number is not prime")
    """
#---------------------------
"""sum=0
i=0
while i<=4:
    s=input("enter a number:")
    n=int(s)
    sum=sum+n
    i=i+1
    print("sum is",sum)"""
#-----------------------
"""sum=0
i=1
while i<=10:
    sum=sum+i
    i=i+1
    print("sum is",sum)
"""
#=================================
"""name = input("What is your name? ")
print("Hello " + name)

job = input("What is your job? ")
print("Your job is " + job)

num = input("Give me a number? ")
print("You said: " + str(num))
"""
#================================
"""import random
MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True
print("Alright...")
while RUNNING:
    GUESS = input("What is your lucky number? ")
    if GUESS.lower() == "exit":
        print("Better luck next time.")
        break
    if int(GUESS) < NUMBER:
        print("Wrong, too low.")
    elif int(GUESS) > NUMBER:
        print("Wrong, too high.")
    elif int(GUESS) == NUMBER:
        print("Yes, that'1s the one, %s." % str(NUMBER))
        if TRY < 2:
            print("Impressive, only %s tries." % str(TRY))
        elif TRY > 2 and TRY < 10:
            print("Pretty good, %s tries." % str(TRY))
        else:
            print("Bad, %s tries." % str(TRY))
        RUNNING = False
    TRY += 1
"""
#=================
"""for i in range(5):   
    num = int(input(f"Enter integer {i+1}: "))
    reversed_num = 0
    temp = num       
    if temp < 0:    
        temp = -temp
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp = temp//10
    if num < 0:      
        reversed_num = -reversed_num
    print("Reversed number:", reversed_num)"""
#------------------
"""n = int(input("How many integers do you want to enter? "))
even_sum = 0
odd_sum = 0
for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    if num % 2 == 0:
        even_sum += num   
    else:
        odd_sum += num    
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
"""
#-----------------------
""""n = int(input("Enter how many terms you want: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")  
    a, b = b, a + b    """
#------------------------
"""marks = int(input("Enter marks (1-100): "))
if marks < 50:
    print("Grade: F")
elif marks >= 50 and marks <= 60:
    print("Grade: E")
elif marks >= 61 and marks <= 70:
    print("Grade: D")
elif marks >= 71 and marks <= 80:
    print("Grade: C")
elif marks >= 81 and marks <= 90:
    print("Grade: B")
elif marks >= 91 and marks <= 100:
    print("Grade: A")
else:
    print("Invalid input! Please enter marks between 1 and 100.") """
#--------------------------
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is:", factorial)