# ASSIGNMENT 01: ARRAYS
# An array is a special variable, which can hold more than one value at a time. Arrays are
# the most commonly used data structure for many reasons.
# First, we look at the basics of how data is inserted, searched, and deleted from arrays.
# Then, we look how the data can be stored in ascending (or descending) key order. This arrangement makes possible a fast way of searching for a data item: the binary search.

# Exercise 1: implement a function that iterates through the array and prints every time in the array
def printArray(array):
    [print(item) for item in array]


# Exercise 2: implement a function that returns number of items in the array
def getCount(array):
    return len(array)


# Exercise 3: implement a function that returns the value at index n
def getItem(array, index):
    return array[index]


# Exercise 4: implement a function that replaces an item at index n and return the array. return -1 if index is out of bound e.g., larger than the array size (do not use any python built-in function)
def replaceItem(array, index, item):
    if index >= len(array):
        return -1
    array[index] = item
    return array


# Exercise 5: implement a function that adds an item at the end of the list (do not use any python built-in function e.g. append)
def addItemAtEnd(array, item):
    array += [item]
    return array


# Exercise 6: implement a function that adds an item at index n and return the array, if n is larger than the size of the array, then insert the item at the end of the array (do not use any python array built-in function e.g. insert)
def addItem(array, index, item):
    if index >= len(array):
        array += [item]
    else:
        array[index] = item
    return array


# Exercise 7: implement a function that returns the index of the (first) element with the specified value. Return -1 if the value was not found (do not use any python built-in function e.g. index)
def findIndex(array, item):
    for i in range(len(array)):
        if item == array[i]:
            return i
    return -1


# Exercise 8: implement a function that deletes the first item with the specified value, return the array if value was found and deleted, -1 otherwise. (do not use any python built-in function)
def delete(array, item):  # Delete first occurrence
    for i in range(len(array)):
        if array[i] == item:
            array = array[:i] + array[i + 1:]
            return array
    return -1


# Exercise 9: implement a function that removes the element at the specified position. Default position value is -1, which returns the last item. The function returns removed value. (do not use any python built-in function)
def deleteAt(array, index=-1):
    if index < 0:
        item = array[len(array)-1]
        array = array[:len(array)-1]
        return item
    elif len(array) > index > -1:
        array = array = array[:index] + array[index + 1:]
        return array[index]


# Exercise 10: implement a function that sorts the list in ascending order.(do not use any python built-in function)

def swap(array, j, k):  # Swap the values at 2 indices
    if (0 <= j and j < len(array) and 0 <= k and k < len(array)):
        array[j], array[k] = array[k], array[j]


# Exercise 10_1: implement a function that implement bubble sorting
def bubbleSort(array):  # Sort comparing adjacent vals
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)


# Exercise 10_2: implement a function that implement selection sorting
def selectionSort(array):  # Sort by selecting min and
    n = len(array)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        swap(array, min_index, i)


# Exercise 11: You are asked to improve the find_index function of Exercise 7. Assuming the array is sorted, implement binary search to returns the index of the (first) element with the specified value. Return -1 if the value was not found (do not use any python built-in function)
def findSortedArray(array, item):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + right // 2
        if item == array[mid]:
            return mid
        elif item < array[mid]:
            right = mid - 1
        elif item > array[mid]:
            left = mid + 1

    return -1

# if __name__ == '__main__':
#     test_append.test_append()
#     test_count.test_count()
#     test_delete.test_delete()
#     test_deleteAt.test_delete_at()
#     test_deleteAt.test_delete_at2()
#     test_deleteAt.test_delete_at3()
#     test_find.test_find()
#     test_find.test_find2()
#     test_findSorted.test_find_sorted()
#     test_findSorted.test_find_sorted2()
#     test_insert.test_insert()
#     test_print.test_print()
#     test_replaceItem.test_count()
#     test_replaceItem.test_count2()
#     test_replaceItem.test_count3()
#     test_findSorted.test_find_sorted()
#     test_findSorted.test_find_sorted2()