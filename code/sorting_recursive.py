#!python
import random

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if (len(items) <= 0):
        return True
    # TODO: Check that all adjacent items are in order, return early if so
    prev = items[0]
    for i in range(1,len(items)):
        if (items[i] < prev):
            return False
        prev = items[i]
    return True

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    m = len(items1), n = len(items2), N = min(m,n)*min(m,n)
    TODO: Running time: O(N) Why and under what conditions?
    TODO: Memory usage: O(m+n) because result is a new list consisting of all the elements"""
    result = []
    # Repeat until one list is empty
    while (len(items1) > 0 and len(items2) > 0): # O(min(m,n)*min(m,n))
        # Find minimum item in both lists and append it to new list
        if (items1[0] > items2[0]):
            item = items2.pop(0) # O(m)
            result.append(item)
            
        else:
            item = items1.pop(0) # O(n)
            result.append(item)
    
    # Append remaining items in non-empty list to new list
    if (len(items1) > 0):
        result.extend(items1)
    if (len(items2) > 0):
        result.extend(items2)
        
    return result


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O((n**2)logn) Why and under what conditions?
    TODO: Memory usage: O(nlogn) because it creates upper and lower new lists"""
    # Split items list into approximately equal halves
    mid = len(items)//2
    upper = items[:mid]
    lower = items[mid:]
    # Sort each half using any other sorting algorithm
    upper.sort()
    lower.sort()
    # Merge sorted halves into one list in sorted order
    items[:] = merge(upper,lower)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(NlogN) Why and under what conditions?
    TODO: Memory usage: O(NlogN) because it creates upper and lower new lists"""
    # Check if list is so small it's already sorted (base case)
    if (len(items) < 2):
        return
    # Split items list into approximately equal halves
    mid = len(items)//2
    upper = items[:mid]
    lower = items[mid:]
    # Sort each half by recursively calling merge sort
    merge_sort(upper) #O(NlogN)
    merge_sort(lower) #O(NlogN)
    # Merge sorted halves into one list in sorted order
    items[:] = merge(upper,lower) #O(N)

def partitionRandomPiv(items, low, high):
    piv_index = low + (high-low)/2
    pivot = items[piv_index]
    print("pivot index: ", piv_index)
    for i in range(low, piv_index):
        print('i',i)
        # Move items greater than pivot into back of range [p+1...high]
        if (items[i] >= pivot):
            print('here')
            item = items.pop(i)
            print(item)
            items.insert(piv_index, item)
            piv_index -= 1
        print(items)

    print("after")
    for i in range(piv_index+1, high):
        print('i', i)
        # Move items less than pivot into front of range [low...p-1]
        if (items[i] < pivot):
            item = items.pop(i)
            items.insert(low, item)
            piv_index += 1
        print(items)

    return piv_index


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (first element in the array) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(N) because it loops through and checks each item in the array
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Choose a pivot any way and document your method in docstring above
    pivot = items[low]
    piv_index = low
    # Loop through all items in range [low...high]
    for i in range(low+1, high):
        # TODO: Move items less than pivot into front of range [low...p-1]
        if (items[i] < pivot):
            item = items.pop(i)
            items.insert(low, item)
            piv_index += 1
        # Move items greater than pivot into back of range [p+1...high]
        # Since we chose the first element as the pivot, this is done for us
    # Move pivot item into final position [p] and return index p
    # Since we chose the first element, this is also done
    return piv_index

# quick sort notes:
    # divide:
        # select a pivot to compare items to
        # partition all items into 2 groups
            # items <= pivot
            # items > pivot
        # [5, 2, 8, 7, 1, 9, 3] pivot: 5
            # [2, 1, 3] and [8, 7, 9]
    # conquer:
        # sort the two groups with quick sort recursively
    # combine:
        # concatenate lesser group, pivot, greater group
        # list1 + pivot + list2
        # [1, 2, 3] + [5] + [7, 8, 9]
def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
     Worst case running time: O(N**2) In the worst case, it will run quick sort N times.
    TODO: Memory usage: O(1) because I'm not allocating new arrays"""
    # Check if high and low range bounds have default values (not given)
    if (low == None):
        low = 0
    if (high == None):
        high = len(items)
    # Check if list or range is so small it's already sorted (base case)
    if (high-low < 2 or is_sorted(items)): # O(N)
        return
    # Partition items in-place around a pivot and get index of pivot
    pivot_index = partition(items, low, high) # O(N)
    # pivot_index = partitionRandomPiv(items, low, high) # O(N)
    # Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, pivot_index)
    quick_sort(items, pivot_index+1, high)
    return
    


if __name__ == '__main__':
    L1 = [4,7,2,8,1,3,2,5]
    merge_sort(L1)
    print(L1)
    L2 = [4,7,2,8,1,3,2,5,6,7,3,436,22,2,45,67]
    merge_sort(L2)
    print(L2)
    L3 = [4,7,2,8,1,3,2,5]
    quick_sort(L3)
    print(L3)
    L4 = [4,7,2,8,1,3,2,5,6,7,3,436,22,2,45,67]
    quick_sort(L4)
    print(L4)

