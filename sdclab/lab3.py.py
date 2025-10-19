#============================================
List = []
print("Blank List: ")
print(List)
List = [10, 20, 14]
print("\nList of numbers: ") 
print(List)
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])  # Accessing first element
print(List[2])  # Accessing third element
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ") 
print(List)
#===========================================
list=[1,2,4,4,3,3,3,6,5]
print("\nlist with the use of numbers")
print(list)
list=[1,2,'greek',4,'for',6,'greeks']
print("\nlist with the use of mixed values:")
print(list)
#===========================================
# Creating a List
List1 = []
print(len(List1))
#Creating a List of numbers 
List2 = [10, 20, 14] 
print(len(List2))
#============================================
my_list = []
print("Initial blank List:")
print(my_list)
my_list.append(1)
my_list.append(2)
my_list.append(4)
print("\nList after addition of three elements:")
print(my_list)
for i in range(1, 4):
    my_list.append(i)
print("\nList after addition of elements from 1-3:")
print(my_list)
my_list.append((5, 6))
print("\nList after addition of a Tuple:")
print(my_list)
list2 = ['For', 'Geeks']
my_list.append(list2)
print("\nList after addition of another List:")
print(my_list)
#===============================================
List =[1,2,3,4]
print("Initial List: " )
print(List)
# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)
#==================================================
list=[1,2,3,4]
print("initial list:")
print(list)
list.extend([8,'greeks','always'])
print("\nlist after performing extend operation:")
print(list)
#========================================================
# Python program to demonstrate
# accessing of element from list
# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
# accessing a element from the # list using index number
print("Accessing a element from the list" )
print(List[0])
print(List[2])
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi -Dimensional list" )
print(List[0][1])
print(List[1][0])
#=======================================
List = [1,2,'Geeks',4, 'For',6, 'Geeks']
print("accessing element using negative indexing")
print(list[-1])
print(list[-3])
#==============================================
# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List = [1, 2, 3, 4, 5, 6,
7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)
# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List)
# Removing elements from List
# using iterator method for i in range(1, 5):
List.remove(i) 
print("\nList after Removing a range of elements: ")
print(List)
#===================================================
List = [1,2,3,4,5]
# Removing element from the
# Set using the pop() method
List .pop()
print (" \nList after popping an element: " )
print ( List)
list.pop(2)
print("list after popping spoecific elemets")
print(list)
#==================================================
# Creating a List
List = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List:") 
print(List)

# Slicing elements in a range 3-8
print("\nSlicing elements in a range 3-8:")
Sliced_List = List[3:9]
print(Sliced_List)

# Print elements from a pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th element till the end:")
print(Sliced_List)

# Printing elements from beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation:")
print(Sliced_List)

#======================================================
List = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List)
# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)
# Print elements of a range
# using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)
# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)
#===============================================
# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict)
#====================================================
# Creating an empty Dictionary
Dict = {}
print ("Empty Dictionary: " )
print ( Dict )
# Creating a Dictionary
# with dict() method
Dict = dict ({ 1: 'Geeks' , 2: 'For' , 3: 'Geeks' })
print (" \nDictionary with the use of dict(): " )
print ( Dict )
# Creating a Dictionary
# with each item as a Pair
Dict = dict ([( 1 , 'Geeks') , ( 2, 'For' )])
print (" \nDictionary with each item as a pair: " )
print ( Dict)
#======================================
# Creating a Nested Dictionary
# as shown in the below image
Dict = {1: 'Geeks', 2: 'For',
3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}
print(Dict)
#==============================================
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ") 
print(Dict)
# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For' 
Dict[3] = 1
print("\nDictionary after adding 3 elements:")
print(Dict)
# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4 
print("\nDictionary after adding 3 elements: ") 
print(Dict)
# Updating existing Key's Value
Dict[2] = 'Welcome' 
print("\nUpdated key value: ")
print(Dict)
# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
print ( "\nAdding a Nested Key: ")
print ( Dict)
#=======================================================
# Python program to demonstrate
# accessing a element from a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("Accessing a element using key:")
print(Dict[1])
print("Accessing a element using key:") 
print(Dict[1])
#===============================================
# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# accessing a element using get()
# method 
print("Accessing a element using get:") 
print(Dict.get(3))
#--------------------------------------------
# Creating a Dictionary
Dict = {
    'Dict1': {1: 'Geeks'},
    'Dict2': {'Name': 'For'}
}
print(Dict['Dict1'])          
print(Dict['Dict1'][1])       
print(Dict['Dict2']['Name'])  
#-------------------------------------------
# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
'B' : {1 : 'Geeks', 2 : 'Life'}}
print("Initial Dictionary: ") 
print(Dict)
# Deleting a Key value del
Dict[6]
print("\nDeleting a specific key: ")
print(Dict)
# Deleting a Key from
# Nested Dictionary del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)
#-------------------------------------------
# Creating a Dictionary
Dict = { 1: 'Geeks' , 'name': 'For' , 3 :
'Geeks' }
pop_ele = Dict .pop( 1)
print ( '\nDictionary after deletion: ' + str( Dict ))
print ( 'Value associated to poped key is: ' + str (pop_ele))
#-------------------------
# Creating Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
pop_ele = Dict.popitem()
print("\nDictionary after deletion: " + str(Dict))
print ("The arbitrary pair returned is: " + str (pop_ele))
#---------------------
# Creating a Dictionary
Dict = { 1: 'Geeks' , 'name': 'For' , 3 : 'Geeks' }
Dict .clear()
print (" \nDeleting Entire Dictionary: " )
print ( Dict)
#-------------------------------
# Accept two lists from the user and display their join
list1 = input("Enter elements of first list separated by spaces: ").split()
list2 = input("Enter elements of second list separated by spaces: ").split()
joined_list = list1 + list2
print("The joined list is:", joined_list)
#------------------------------------
# Given matrices
a = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# Create an empty result matrix with all zeros
c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

# Matrix multiplication
for i in range(len(a)):          # rows of a
    for j in range(len(b[0])):   # columns of b
        for k in range(len(b)):  # rows of b
            c[i][j] += a[i][k] * b[k][j]

# Display result
print("Product of matrices A and B is:")
for row in c:
    print(row)
#=============================================
# Dictionary with tuple keys (first name, last name)
phone_book = {
    ('ali', 'khan'): '0300-1234567',
    ('sara', 'ahmed'): '0321-9876543',
    ('bilal', 'hussain'): '0333-4567890'
}

while True:
    # Ask user for input
    first = input("Enter first name: ").strip().lower()
    last = input("Enter last name: ").strip().lower()

    key = (first, last)

    # Search in the dictionary
    if key in phone_book:
        print(f"✅ Phone number of {first.title()} {last.title()} is: {phone_book[key]}")
        break
    else:
        print(f"Sorry, phone number for {first.title()} {last.title()} not found.")
        again = input("Do you want to try again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break
#=========================================
# Create two empty lists
list1 = []
list2 = []

n1 = int(input("How many elements in the first list? "))
for i in range(n1):
    value = int(input(f"Enter element {i+1} for first list: "))
    list1.append(value)

# Take input for second list
n2 = int(input("How many elements in the second list? "))
for i in range(n2):
    value = int(input(f"Enter element {i+1} for second list: "))
    list2.append(value)

# Merge the two lists
merged_list = list1 + list2
# Sort the merged list
merged_list.sort()

print("The merged and sorted list is:", merged_list)
#================================================
# Create two empty lists
list1 = []
list2 = []

# Take input for first list
n1 = int(input("How many elements in the first list? "))
for i in range(n1):
    value = int(input(f"Enter element {i+1} for first list: "))
    list1.append(value)

# Take input for second list
n2 = int(input("How many elements in the second list? "))
for i in range(n2):
    value = int(input(f"Enter element {i+1} for second list: "))
    list2.append(value)

# Merge both lists
merged_list = list1 + list2

# Display merged list
print("\nMerged list:", merged_list)

# Find smallest and largest
smallest = merged_list[0]
largest = merged_list[0]

for num in merged_list:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

# Display results
print("Smallest element:", smallest)
print("Largest element:", largest)

