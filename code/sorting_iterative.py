#!python


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


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    for i in range(len(items)):
        # moves the largest item at the end each time
        for j in range(len(items)):
            if (j < len(items)-1 and items[j] > items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]

    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    for i in range(len(items)):
        # find min element
        temp = i
        for j in range(i, len(items)):
            if (items[temp] > items[j]):
                temp = j
        # swap
        items[i], items[temp] = items[temp], items[i]
    
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for i in range(len(items)):
        # chosen item = items[i]
        # swap item with prev until prev is less than item
        j = i # track item index
        while (j > 0 and items[j] < items[j-1]):
            items[j-1], items[j] = items[j], items[j-1]
            j -= 1
    return items
