# Program to find a pair of numbers which sum to a given number. Input non distinct array, output list of pairs

# Approach 1: using dictionary to save difference 
def two_sum_dict(target, array):
    difference = {}
    pairs = []
    
    for num in array:
        diff = target - num
        if num in difference:
            pairs.append((num, diff))
        else:
            difference[diff] = num
    print(pairs)
    
    # Approach 2: using sort & pointers
def two_sum_sort(target, array):
    pairs = []
    array.sort()
    i,j = 0, len(array)-1
    while i<j:
        sum = array[i]+array[j]
        if sum == target:
            pairs.append((array[i], array[j]))
            i+=1
            j-=1
        if sum > target:
            j-=1
        if sum < target:
            i+=1
    print(pairs)             


if __name__ == '__main__':
    target = 10
    array = [3, 5, -4, 8, 11, 1, -1, 6, 5]
    two_sum_dict(target, array)
    two_sum_sort(target, array)
