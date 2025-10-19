#=========================================
def reverse_string(s):
    """This function takes a string and returns it in reverse order."""
    return s[::-1] 

word = "hello"
reversed_word = reverse_string(word)
print("The reverse of", word, "is", reversed_word)




#-------------------------------------------
def is_even(number):
    """
    This function takes an integer as input.
    It returns True if the number is even, and False if it is odd.
    """
    if number % 2 == 0:
        return True   
    else:
        return False  

num = int(input("Enter an integer: "))

if is_even(num):
    print(num, "is an Even number.")
else:
    print(num, "is an Odd number.")




def sum_list(numbers):
    """
    This function takes a list of numbers as input.
    It adds each number in the list to a total variable
    and finally returns the total sum.
    """
    total = 0  

    for num in numbers:
        total += num  

    return total

my_numbers = [5, 10, 15, 20, 25]
result = sum_list(my_numbers)
print("List of numbers:", my_numbers)
print("Sum of all numbers:", result)






def calculate_rectangle_area(length, width):
    """
    This function takes two arguments:
    - length: the length of the rectangle
    - width: the width of the rectangle
    It returns the area of the rectangle using the formula:
        area = length * width
    """
    area = length * width  
    return area            
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
result = calculate_rectangle_area(length, width)
print("----------------------------------")
print("Length:", length)
print("Width :", width)
print("Area of the Rectangle =", result)
print("----------------------------------")


# -----------------------------------------------
# Function Name: count_vowels
# Purpose: To count the total number of vowels (a, e, i, o, u)
# in a given string, ignoring case.
# -----------------------------------------------

def count_vowels(text):
    """
    This function takes a string as input and counts how many vowels
    (a, e, i, o, u) are present in it, regardless of uppercase or lowercase.
    It returns the total count of vowels.
    """
    vowels = "aeiou"
    count = 0
    text = text.lower()
    for char in text:
        if char in vowels:  
            count += 1       
    return count
user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
print("----------------------------------")
print("Entered String :", user_input)
print("Total Vowels   :", vowel_count)
print("----------------------------------")
