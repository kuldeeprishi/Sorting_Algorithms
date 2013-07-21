#-------------------------------------------------------------------------------
# Name     :    Selection Sort
# Purpose  :    in-place comparison sort
#
# Performance:
# ============
# Worst case       :	 O(n^2)
# Best case 	   :     O(n^2)
# Average case     :     O(n^2)
# Worst case space
# complexity       :	 O(n) total, O(1) auxiliary
#
# Author           :     Kuldeep Rishi
# Created          :     21-07-2013
# More info        :     http://en.wikipedia.org/wiki/Selection_sort
#-------------------------------------------------------------------------------

def selection_sort(list):
    for i in xrange(len(list)):
        smallest_elt = i # assume smallest elt is at i
        for j in xrange(i, len(list)): # search for smallest elt in list
            if list[j] < list[smallest_elt]: # is val at index j is smaller
                smallest_elt = j  # update smallest elt index
        list[i], list[smallest_elt] = list[smallest_elt], list[i] # swap
    return list



# Example Implementaion of Selection sort
l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print 'original list        ==>  ', l
selection_sort(l)
print 'after Selection sort ==>  ', l
