#-------------------------------------------------------------------------------
# Name     :   Bubble Sort
# Purpose  :   A simple sorting algorithm that works by repeatedly stepping
#              through the list to be sorted, comparing each pair of adjacent
#              items and swapping them if they are in the wrong order. The pass
#              through the list is repeated until no swaps are needed, which
#              indicates that the list is sorted.
#
# Performance:
# ============
# Worst case       :	 O(n^2)
# Best case 	   :     O(n)
# Average case     :     O(n^2)
# Worst case space
# complexity       :	 O(1) auxiliary
#
# Author           :     Kuldeep Rishi
# Created          :     21-07-2013
# More info        :     http://en.wikipedia.org/wiki/Bubble_sort
#-------------------------------------------------------------------------------


# Bubble sort: Larger element in list bubble upto the top
def bubble_sort(list):
    list_sorted = False
    while not list_sorted: # Repeat till list is sorted
        list_sorted = True
        for i in xrange(1, len(list)):
            if list[i-1] > list[i]:     # if prev elt is greater then
                list[i-1], list[i] = list[i], list[i-1]  # swap them
                list_sorted = False
    return list




# Example Implementaion of Bubble sort
l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print 'original list      ==>  ', l
bubble_sort(l)
print 'bubble sorted list ==>  ', l