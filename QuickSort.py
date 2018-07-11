# Global Variables
totalNumberComparison = 0


def partition1(arr, l, r):
    assert l==0
    p = arr[l]
    i = l+1
    for j in range(l+1, r+1):
        if arr[j] < p:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i = i+1
        # print(arr)
    temp = arr[l]
    arr[l] = arr[i-1]
    arr[i-1] = temp
    return arr[:i-1], arr[i-1], arr[i:]

def partition2(arr, l, r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp
    p = arr[l]
    i = l+1
    for j in range(l+1, r+1):
        if arr[j] < p:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i = i+1
        # print(arr)
    temp = arr[l]
    arr[l] = arr[i-1]
    arr[i-1] = temp
    return arr[:i-1], arr[i-1], arr[i:]


def choosePivot(arr):
    # median of three pivot
    first_element = arr[0]
    last_element = arr[len(arr)-1]
    idx = (len(arr)-1) // 2
    median_element = arr[idx]
    median = sorted([first_element, last_element, median_element])[1]
    pivot = median
    return pivot

def partition3(arr, l, r):
    p = choosePivot(arr)
    first = arr[0]
    arr[0] = p
    i = l+1
    for j in range(l+1, r+1):
        if arr[j] == p:
            arr[j] = first
        if arr[j] < p:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i = i+1
        # print(arr)
    temp = arr[l]
    arr[l] = arr[i-1]
    arr[i-1] = temp
    return arr[:i-1], arr[i-1], arr[i:]

def quickSort(arr):
    '''
    partition:
    1: first element as pivot
    2: last element as pivot
    3: median of three rule
    '''
    if len(arr) <= 1:
        return arr
    # p = choosePivot(arr)
    first_part, p, second_part = partition3(arr, 0, len(arr)-1)
    global totalNumberComparison 
    totalNumberComparison += len(arr) - 1
    arr[:len(first_part)] = quickSort(first_part)
    arr[len(first_part)+1:] = quickSort(second_part)
    return first_part+ [p]+ second_part


if __name__ == '__main__':
    text_file = open("quicksort_input.txt")
    pa3 = text_file.read().split()
    pa3 = [int(x) for x in pa3]
    print(type(pa3[0]))

    a = [5,1,3, 0, 7,2,4]
    print(partition3(a,0,len(a)-1))
    sorted_array = quickSort(pa3)
    # # print(sorted_array)
    assert sorted(pa3) == sorted_array 
    print(totalNumberComparison)
    # print('HERE')


