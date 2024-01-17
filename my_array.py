# ASSIGNMENT 01: ARRAYS
# An array is a special variable, which can hold more than one value at a time. Arrays are 
# the most commonly used data structure for many reasons.
# First, we look at the basics of how data is inserted, searched, and deleted from arrays. 
# Then, we look how the data can be stored in ascending (or descending) key order. This arrangement makes possible a fast way of searching for a data item: the binary search.

#Exercise 1: implement a function that iterates thourgh the array and prints every time in the array
def printArray(array):
   ## ADD YOUR CODE HERE

#Exercise 2: implement a function that returns number of items in the array
def getCount(array):
   ## ADD YOUR CODE HERE

#Exercise 3: implement a function that returns the value at index n
def getItem(array, index):
    ## ADD YOUR CODE HERE

#Exercise 4: implement a function that replaces an item at index n and return the array. return -1 if index is out of bound e.g., larger than the array size (do not use any python built-in function)
def replaceItem(array, index, item):
    ## ADD YOUR CODE HERE

#Exercise 5: implement a function that adds an item at the end of the list (do not use any python built-in function e.g. append)
def addItemAtEnd(array, item):
    ## ADD YOUR CODE HERE 
    

#Exercise 6: implement a function that adds an item at index n and return the array, if n is larger than the size of the array, then insert the item at the end of the array (do not use any python array built-in function e.g. insert)
def addItem(array, index, item):
    ## ADD YOUR CODE HERE


#Exercise 7: implement a function that returns the index of the (first) element with the specified value. Return -1 if the value was not found (do not use any python built-in function e.g. index)
def findIndex(array, item):
    ## ADD YOUR CODE HERE


#Exercise 8: implement a function that deletes the first item with the specified value, return the array if value was found and deleted, -1 otherwise. (do not use any python built-in function)
def delete(array, item):             # Delete first occurrence
    ## ADD YOUR CODE HERE


#Exercise 9: implement a function that removes the element at the specified position. Default position value is -1, which returns the last item. The function returns removed value. (do not use any python built-in function)
def deleteAt(array, index= -1):
    ## ADD YOUR CODE HERE


#Exercise 10: implement a function that sorts the list in ascending order.(do not use any python built-in function)

def swap(array, j, k):# Swap the values at 2 indices
    if (0 <= j and j < len(array) and 0 <= k and k < len(array)): 
        array[j], array[k] = array[k], array[j]
         
#Exercise 10_1: implement a function that implement bubble sorting
def bubbleSort(array):               # Sort comparing adjacent vals
    ## ADD YOUR CODE HERE
            
#Exercise 10_2: implement a function that implement selection sorting
def selectionSort(array):           # Sort by selecting min and 
    ## ADD YOUR CODE HERE

#Exercise 11: You are asked to improve the find_index function of Exercise 7. Assuming the array is sorted, implement binary search to returns the index of the (first) element with the specified value. Return -1 if the value was not found (do not use any python built-in function)
def findSortedArray(array, item):             # Find index at or just below key
    ## ADD YOUR CODE HERE

