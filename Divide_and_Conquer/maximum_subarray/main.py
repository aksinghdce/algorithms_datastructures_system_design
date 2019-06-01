#!python
'''
Step1: Randomly generate 10 samples of inputs with increasing number of change elements in a specific range
Step2: Run both "recursive" and "non-recursive" algorithm on the 10 samples and calculate the average amount of time.
Step3: Plot the average amount of time for the algorithms and find the crossover point
Step4: At crossover point switch the algorithm and then measure time.
'''
from maximum_subarray.maximum_subarray_nonrecursive.maximum_subarray_nonrecursive import find_maximum_subarray as nonrec
from maximum_subarray.maximum_subarray_recursive.maximum_subarray_recursive import find_maximum_subarray as rec
import random
import timeit
def get_input_of_size(n:int):
    v:list = list()
    i:int = 0
    for i in range(n):
        v.append(random.randint(-99, 20))
    return v
if __name__ == '__main__':
    total_rec:float = 0.0
    total_nonrec:float = 0.0
    N:int = 200
    for i in range(1, N, 1):
        arr = get_input_of_size(i)
        rec_time:float = timeit.timeit('rec(arr,0,i-1)',
                      'from __main__ import ' + ', '.join(globals()),number=10)
        nonrec_time:float = timeit.timeit('nonrec(arr,0,i-1)',
                                       'from __main__ import ' + ', '.join(globals()),number=10)
        if rec_time > nonrec_time:
            print(i)
