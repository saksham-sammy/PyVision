def linear_Search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            print("Element Found")
            return i
        return -1
    

def Binary_Search(lst, target):
    low = 0
    high = len[lst] -1
    while low<=high:
        mid = (low + high) // 2
        if lst[mid]==target:
            print("Element Found")
            return mid
        elif (lst[mid]<target):
            low = mid+1
        else :
            high = mid-1
        return -1
    
words = ["apple", "banana", "cherry", "date", "fig", "grape", "mango"]

target_word = input("Enter word to search (Linear Search): ")
pos1 = linear_Search(words, target_word)
if pos1 != -1:
    print("Linear Search: Element found at index", pos1)
else:
    print("Linear Search: Element not found")
