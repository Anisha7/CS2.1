#!python

    # [5,6,7,8,9]
    # 9-5 = 4
    # [30,40,95,100]
    # 100-30 = 70
def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum integer values)
    print('input: %s'%(str(numbers)))
    minNum = min(numbers)
    maxNum = max(numbers)
    listLen = maxNum - minNum + 1
    # Create list of counts with a slot for each number in input range
    countList = [0]*listLen

    # Loop over given numbers and increment each number's count
    for num in numbers:
        i = num - minNum
        countList[i] += 1
    # Loop over counts and append that many numbers into output list
    j = 0
    for i in range(len(countList)): # O(N)
        count = countList[i]
        while count > 0:
            numbers[j] = i+minNum
            # numbers.append(i + minNum)
            count -= 1
            j += 1
    # Improve this to mutate input instead of creating new output list
    return numbers


    # [15,20,25,30,33,44,50]
    # 50-15 = 35
    # 35//9 + 1 = 4
    # 15 + 4 = 19, everything less than 18 in one bucket
    # 15,   19,   23,   27,   31,   35, 39,   43,   47, 51,
    #   [15], [20], [25], [30], [33], [], [44], [50], [], []
def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum values)
    print('input: %s'%(str(numbers)))
    minNum = min(numbers)
    maxNum = max(numbers)
    totalRange = maxNum - minNum

    # Create list of buckets to store numbers in subranges of input range
    bucket = []
    for i in range(num_buckets):
        bucket.append([])

    # Loop over given numbers and place each item in appropriate bucket
    incr = totalRange//(num_buckets-1)
    if (incr == 0):
        incr = 1

    for num in numbers:
        i = (num-minNum)//incr
        bucket[i].append(num)

    # Sort each bucket using any sorting algorithm (recursive or another)
    for buck in bucket: #m*nlogn, m = buckets, n = items in bucket
        buck.sort() #nlogn
    
    # Loop over buckets and append each bucket's numbers into output list
    i = 0
    for buck in bucket:
        for num in buck:
            numbers[i] = num
            i += 1
    # Improve this to mutate input instead of creating new output list
    return numbers


if __name__ == '__main__':
    L1 = [4,7,2,8,1,3,2,5]
    counting_sort(L1)
    print(L1)
    L2 = [4,7,2,8,1,3,2,5,6,7,3,436,22,2,45,67]
    counting_sort(L2)
    print(L2)
    L3 = [4,7,2,8,1,3,2,5]
    bucket_sort(L3, 3)
    print(L3)
    L4 = [4,7,2,8,1,3,2,5,6,7,3,436,22,2,45,67]
    bucket_sort(L4)
    print(L4)