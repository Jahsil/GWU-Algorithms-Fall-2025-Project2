# import time to measure execution time
import time
import random


# Quickselect algorithm implementation in Python using the Median of Medians approach.
# Time complexity is guaranteed to be O(n) in the worst case.

# this is the insertion sort algorithm to sort the numbers in the list
def insertionSort(num_list):

    # loop through the numbers in the list
    for i in range(1, len(num_list)):

        # select the current number to be compared
        key = num_list[i]

        # compare the current number with the previous number
        j = i - 1

        # as long as the previous number is greater than the current number and j is not less than 0
        while j >= 0 and num_list[j] > key:

            # swap the numbers
            num_list[j + 1] = num_list[j]

            # then decrement j by 1
            j -= 1

        # place the current number in its correct position
        num_list[j + 1] = key

    # finally return the sorted list
    return num_list


def partitionArray(num_list, pivot):
    # define variables for storing the less than, equal to, and greater than lists
    less_than = []

    # equal to list is for storing numbers equal to the pivot if the numbers are not distinct
    equal_to = []
    greater_than = []   

    # loop through the numbers in the list
    for num in num_list:

        # if the current number is less than the pivot
        if num < pivot:

            # add it to the less than list
            less_than.append(num)

        # if the current number is greater than the pivot
        elif num > pivot:

            # add it to the greater than list
            greater_than.append(num)

        # if the current number is equal to the pivot
        else:

            # add it to the equal to list
            equal_to.append(num)

    # finally return the three lists as a tuple
    return (less_than, equal_to, greater_than)


def findMedianOfMedians(nums_list, k):
    # actual function to find the k-th smallest element using the median of medians algorithm

    N = len(nums_list)
    if N <= 5:
        # if the length of the numbers is less than or equal to 5, 
        # just sort it using the insertionSort helper function and return the median
        
        nums_list = insertionSort(nums_list)
        return nums_list[k-1]

    # Divide the array into groups of 5. There are n/5 groups.
    partitions = [nums_list[i:i + 5] for i in range(0, N, 5)]

  
    # Sort the small groups using insertion sort. Since each group is
    # of 5 elements, it takes a constant amount of time to sort those
    # groups.

    # Collect all the n/5 medians from the n/5 groups.
   
    medians = [insertionSort(partition)[len(partition) // 2] for partition in partitions]

    # recursively find the median of the medians
    medianOfMedians = findMedianOfMedians(medians, (len(medians) + 1) // 2)

    #  Partition the array on the median of medians.
    left, equal, right = partitionArray(nums_list, medianOfMedians)

    # recursively call the function based on the value of k
    # if k is less than or equal to the length of the less than list
    # it implies that the k-th smallest element is in the less than list
    if k <= len(left):
        return findMedianOfMedians(left, k)
    
    # if k is greater than the length of the less than list 
    # and less than or equal to the length of the less than list + length of the equal to list
    # it implies that the k-th smallest element is the median of medians
    elif k <= len(left) + len(equal):
        return medianOfMedians
    
    # else it implies that the k-th smallest element is in the greater than list
    # so recursively call the function on the greater than list
    else:
        return findMedianOfMedians(right, k - len(left) - len(equal))


if __name__ == "__main__":

    power = 1
    n = 10 ** power  
    k = n // 2  # Find the median value

    nums_list = [random.randint(1, n * 10) for _ in range(n)]  # Random list of n values
   
    start_time = time.time()
    result = findMedianOfMedians(nums_list, k)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: ", execution_time)
    print(f"The {k}th smallest number is :", result)
