#-------------------------------------------------------------------------------
# Name     :    Merge Sort
# Purpose  :    comparison-based sorting algorithm
#               return a sorted list does not modify original list
#
# Performance:
# ============
# Worst case       :    O(n log n)
# Best case 	   :    O(n log n) typical, O(n) natural variant
# Average case     :    O(n log n)
# Worst case space
# complexity       :    O(n) auxiliary
#
# Author           :     Kuldeep Rishi
# Created          :     21-07-2013
# More info        :     http://en.wikipedia.org/wiki/Merge_sort
#-------------------------------------------------------------------------------

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # compare i and j elt of left and right
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):  # append remaining element of left
        result.append(left[i])
        i += 1
    while j < len(right): # # append remaining element of right
        result.append(right[j])
        j += 1
    return result

def merge_sort(list):
    if len(list) == 1:
        return list
    mid = len(list)/2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)




# Example Implementaion of Selection sort
l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print 'original list      ==>  ', l
l = merge_sort(l)  # merge_sort return a sorted list does not modify original list
print 'after merge sort   ==>  ', l
