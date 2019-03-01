# create all possible sums of the sets of 3 given
# add them to the dictionary counts as [sum] : count
def sumRec(L, m, counts, low, s=0, depth=''):
    if m == 0:
        # increment or initialize count for sum
        if s in counts.keys():
            counts[s] += 1
        else:
            counts[s] = 1
            # get depth for better debugging
            print(depth + 'sum: ' + str(s))
        return
    
    # get each possible sum
    for i in range(low, len(L)-m+1):
        # s tracks the current sum$
        s += L[i]
        print(depth + str(L[i]))
        # increment i to make all posibilities with the next item in list
        sumRec(L, m-1, counts, i+1, s, depth+' ')
        s -= L[i]
    return

# Main function for summing the sets (S is converted to list before passed in)
def summ(S, m):
    counts = dict() # dictionary to track counts of sums
    low = 0
    sumRec(S, m, counts, low)
    result = 0
    for key in counts:
        # find sums that occured only once and add those to result
        if counts[key] == 1:
            result += key
    return result

    