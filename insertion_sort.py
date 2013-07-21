#-------------------------------------------------------------------------------
# Name     :    Insertion Sort
# Purpose  :    Insertion sort is a simple sorting algorithm that builds the
#               final sorted array (or list) one item at a time. Insertion sort
#               iterates, consuming one input element each repetition, & growing
#               a sorted output list. On a repetition, insertion sort removes one
#               element from the input data, finds the location it belongs within
#               the sorted list, and inserts it there. It repeats until no input
#               elements remain.
#
#
# Performance:
# ============
# Worst case       :	 O(n^2) comparisons, swaps
# Best case 	   :     O(n) comparisons, O(1) swaps
# Average case     :     O(n^2) comparisons, swaps
# Worst case space
# complexity       :	 O(n) total, O(1) auxiliary
#
# Author           :     Kuldeep Rishi
# Created          :     21-07-2013
# More info        :     http://en.wikipedia.org/wiki/Insertion_sort
#-------------------------------------------------------------------------------

def insertion_sort(list):
    for i in range(1, len(list)): # We maintain a sorted list at begining
        val = list[i]       # hold value at i in temp temporarily
        j = i - 1
        while j >= 0 and list[j] > val: # prev elt is greater than val
            list[j+1] = list[j]         # shift the elements
            j -= 1
        list[j+1] = val                # set the val to its desired location
    return list



# Example Implementaion of Insertion sort
l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print 'original list        ==>  ', l
insertion_sort(l)
print 'after insertion sort ==>  ', l
