#!python

from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort
from sorting_recursive import split_sort_merge, merge_sort, quick_sort
from sorting_integer import counting_sort, bucket_sort


# def is_sorted(items):
#     """Return a boolean indicating whether given items are in sorted order.
#     Running time: O(N) Why and under what conditions?
#     Memory usage: O(1) Why and under what conditions?"""
#     # TODO: Check that all adjacent items are in order, return early if not
#     if (items == None): return True
#     prev = None
#     for i in range(0,len(items)):
#         if prev == None:
#             prev = items[i]
#         if (items[i] < prev):
#             return False
#         prev = items[i]
#     return True


# def bubble_sort(items):
#     """Sort given items by swapping adjacent items that are out of order, and
#     repeating until all items are in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Swap adjacent items that are out of order

#     for i in range(len(items)):
#         # moves the largest item at the end each time
#         for j in range(len(items)):
#             if (j < len(items)-1 and items[j] > items[j+1]):
#                 items[j], items[j+1] = items[j+1], items[j]

#     return items

# def selection_sort(items):
#     """Sort given items by finding minimum item, swapping it with first
#     unsorted item, and repeating until all items are in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Find minimum item in unsorted items
#     # TODO: Swap it with first unsorted item
#     for i in range(len(items)):
#         # find min element
#         temp = i
#         for j in range(i, len(items)):
#             if (items[temp] > items[j]):
#                 temp = j
#         # swap
#         items[i], items[temp] = items[temp], items[i]
    
#     return items


# def insertion_sort(items):
#     """Sort given items by taking first unsorted item, inserting it in sorted
#     order in front of items, and repeating until all items are in order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Take first unsorted item
#     # TODO: Insert it in sorted order in front of items
#     for i in range(len(items)):
#         # chosen item = items[i]
#         # swap item with prev until prev is less than item
#         j = i # track item index
#         while (j > 0 and items[j] < items[j-1]):
#             items[j-1], items[j] = items[j], items[j-1]
#             j -= 1
#     return items


# def merge(items1, items2):
#     """Merge given lists of items, each assumed to already be in sorted order,
#     and return a new list containing all items in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until one list is empty
#     # TODO: Find minimum item in both lists and append it to new list
#     # TODO: Append remaining items in non-empty list to new list
#     result = []
#     while (len(items1) != 0 and len(items2) != 0):
#         if (items1[0] > items2[0]):
#             result.append(items2[0])
#             items2 = items2[1:]
#         else:
#             result.append(items1[0])
#             items1 = items1[1:]
    
#     if (len(items1) > 0):
#         result += items1
#     if (len(items2) > 0):
#         result += items2
        
#     return result


# def split_sort_merge(items):
#     """Sort given items by splitting list into two approximately equal halves,
#     sorting each with an iterative sorting algorithm, and merging results into
#     a list in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Split items list into approximately equal halves
#     mid = len(items)//2
#     upper = items[:mid]
#     lower = items[mid:]
#     # TODO: Sort each half using any other sorting algorithm
#     upper.sort()
#     lower.sort()
#     # TODO: Merge sorted halves into one list in sorted order
#     result = merge(upper,lower)
#     items = result
#     return items


# def merge_sort(items):
#     """Sort given items by splitting list into two approximately equal halves,
#     sorting each recursively, and merging results into a list in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Check if list is so small it's already sorted (base case)
#     if (len(items) < 2):
#         return items
#     # TODO: Split items list into approximately equal halves
#     mid = len(items)//2
#     upper = items[:mid]
#     lower = items[mid:]
#     # TODO: Sort each half by recursively calling merge sort
#     upper = merge_sort(upper)
#     lower = merge_sort(lower)
#     # TODO: Merge sorted halves into one list in sorted order
#     result = merge(upper,lower)
#     items = result
#     return items


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    items = sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()