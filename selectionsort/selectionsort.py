# Ask user to enter 5 elements
size = 5
arr = []
print("Enter 5 elements:")
for i in range(size):
    num = int(input(f"Element {i+1}: "))
    arr.append(num)

for i in range(size - 1):
    min_index = i
    for j in range(i + 1, size):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]  

print("\nSorted array in ascending order:")
print(arr)
