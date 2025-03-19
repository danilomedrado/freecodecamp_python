#learn-data-structures-by-building-the-merge-sort-algorithm
#https://github.com/freeCodeCamp/freeCodeCamp/tree/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-data-structures-by-building-the-merge-sort-algorithm
#In this project, you willl learn data structures by building the merge sort algorithm.

#This is a sorting algorithm that uses the divide-and-conquer principle to sort collections of data. 
#That is, it 'divides' a collection into smaller sub-parts, and 'conquers' the sub-parts by sorting them independently, then merges the sorted sub-parts.
#The merge sort algorithm mainly performs three actions:

#Divide an unsorted sequence of items into sub-parts
#Sort the items in the sub-parts
#Merge the sorted sub-parts
#The above happens recursively until the sub-parts are merged into the complete sorted sequence. Let's start by dividing the sequence.
#The merge sort algorithm mainly performs three actions:
    #Divide an unsorted sequence of items into sub-parts
    #Sort the items in the sub-parts
    #Merge the sorted sub-parts
#The above happens recursively until the sub-parts are merged into the complete sorted sequence. 
#Let's start by dividing the sequence.

def merge_sort(array):
    #Before testing the merge_sort() function, you need to create a base case that stops the function execution when the length of array is less than or equal to 1.
    #This base case will stop the recursion call. Without it, the merge sort operation would continue to run even when the list has been sorted or has no element in it.
    #Right after the function declaration, create an if statement with this condition: len(array) <= 1. Use the pass keyword in the function's body.    
    if len(array) <= 1:
        return
    
    #print('array', array)
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    #print('left_part', left_part)
    #print('right_part', right_part)

    #print('____________________________')

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    #Inside your function, create a while loop that compares an element in left_part to an element in right_part, and merges the smaller element to the main array list.
    #Create two conditions for the loop: one that checks whether the left_array_index is less than the length of left_part and another condition that checks whether right_array_index is less than the length of right_part.    

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        #if statement that checks if the index of left_part is less than the index of right_part.
        #When the if condition evaluates to True, it means that the element in the left_part list is smaller than the element it is being compared to in the right_part list.
        #In that case, you can assign the left_part index to the sorted array.        
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    #The while loop you created compares one element from left_part with another in right_part, then adds the smaller element to the main array list.
    #It will continue this operation until there are no elements left to be compared. But left_part may still have elements left while right_part has none, and vice versa.
    #Create another while loop to copy the remaining elements in left_part into the array list. Use left_array_index < len(left_part) for the while condition.        

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1
    
    #print('array sorted', array)

#You can use the __name__ variable to determine if a Python script is being run as the main program or if it is being imported as a module (code written in another Python file).
#If the value of __name__ is set to '__main__', it implies that the current script is the main program, and not a module.
#In this project, you'll use the current script as the main program.

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))

