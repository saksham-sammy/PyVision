# ----------- Linear Search Function -----------
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# ----------- Binary Search Function -----------
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ----------- MAIN PROGRAM -----------
words = ["apple", "banana", "cherry", "date", "fig", "grape", "mango"]

# Linear Search
target_word = input("Enter word to search (Linear Search): ")
pos1 = linear_search(words, target_word)
if pos1 != -1:
    print("Linear Search: Element found at index", pos1)
else:
    print("Linear Search: Element not found")

# Binary Search
# Binary search works only on a sorted list
words.sort()
print("\nSorted list for Binary Search:", words)
target_word2 = input("Enter word to search (Binary Search): ")
pos2 = binary_search(words, target_word2)
if pos2 != -1:
    print("Binary Search: Element found at index", pos2)
else:
    print("Binary Search: Element not found")
