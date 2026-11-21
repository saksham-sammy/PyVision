# Linear Search using user input

# taking list input
arr = list(map(int, input("Enter the list elements separated by space: ").split()))

# element to search
x = int(input("Enter the element to search: "))

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i     # return index
    return -1

result = linear_search(arr, x)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
