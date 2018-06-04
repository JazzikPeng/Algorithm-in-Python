# mad man problem
import numpy as np


def rand(a, b):
    return np.random.randint(a, b+1, dtype=int)


def mad_man(num):
    a = rand(1, num)
   # print(a)
    if a == 1 or num == 1:
        return True
    elif a == num:
        return False
    else:
        return mad_man(num+1-a)


counter = 0
trials = 100000
for i in range(trials):
    if mad_man(3) == True:
        counter += 1
print(counter / trials)
