
# coding: utf-8
# Author: Zhejian Peng
# Brute Force: double for loop inversion, find the Max. number of Inversion


def inversion(array):
    counter = 0
    for i in range(len(array)):
        temp = array[i+1:]
        for j in temp:
            if array[i] > j:
                counter += 1
    return counter


# recursive method, in O(NlogN)

def merge_and_count(a, b):
    c = []
    counter = 0
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            counter += len(a)
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
        # print(a)
    return c, counter


def fast_inversion(array):
    if len(array) <= 1:
        return array, 0
    else:
        n = len(array)
        half_point = n // 2
        # print(half_point)
        # print(array[0:half_point])
        b, x = fast_inversion(array[:half_point])
        c, y = fast_inversion(array[half_point:])
        d, z = merge_and_count(b, c)
    return d, x+y+z


# Define Test Case:
test0 = [1, 2, 4, 6, 5]
a, b = fast_inversion(test0)
print('test 0', b)

test1 = [1, 3, 5, 2, 4, 6]
a, b = fast_inversion(test1)
print('test 1', b)
assert(b == 3)

test2 = [1, 5, 3, 2, 4]
a, b = fast_inversion(test2)
print('test 2', b)
assert(b == 4)

test3 = [5, 4, 3, 2, 1]
a, b = fast_inversion(test3)
print('test 3', b)
assert(b == 10)

test4 = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
a, b = fast_inversion(test4)
print('test 4', b)
assert(b == 56)

test5 = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97,
         43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
a, b = fast_inversion(test5)
print('test 5', b)
assert(b == 2372)
# Define test case to test speed
# import numpy as np
# test_array = np.linspace(0, 10000, 10000)
# np.random.shuffle(test_array)
# test_array = list(test_array)

# # PA2
text_file = open("input_dgrcode_66_100000.txt")
pa2 = text_file.read().split()
print(len(pa2))
temp, result = fast_inversion(pa2)
print('PA2 result:', result)
print(all(temp[i] <= temp[i+1] for i in range(len(temp)-1))
      )
# assert(result == 2507917401)


xarray = [7, 6, 5, 4, 3]
count = 0


def InversionsCount(x):
    global count
    midsection = int(len(x) / 2)
    leftArray = x[:midsection]
    rightArray = x[midsection:]
    if len(x) > 1:
        InversionsCount(leftArray)
        InversionsCount(rightArray)
        i, j = 0, 0
        a = leftArray
        b = rightArray
        for k in range(len(a) + len(b) + 1):
            if a[i] <= b[j]:
                x[k] = a[i]
                i += 1
                if i == len(a) and j != len(b):
                    while j != len(b):
                        k += 1
                        x[k] = b[j]
                        j += 1
                    break
            elif a[i] > b[j]:
                x[k] = b[j]
                count += (len(a) - i)
                j += 1
                if j == len(b) and i != len(a):
                    while i != len(a):
                        k += 1
                        x[k] = a[i]
                        i += 1
                    break


InversionsCount(pa2)
print(count)
