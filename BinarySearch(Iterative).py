# Binary Search using user input

# taking list input
arr = list(map(int, input("Enter sorted list elements separated by space: ").split()))

# element to search
x = int(input("Enter the element to search: "))

def binary_search(arr, x):
    l, h = 0, len(arr) - 1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            h = mid - 1
    return -1

result = binary_search(arr, x)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
