#!python
'''
Algorithm:
    Step 1: initialize li=0, ui = 0, sum_j = 0, nli = 0, nui = 0, sum_k = 0
    Step 2: iterate from the beginning of the array by taking k from 1 to n and update nli, nui and sum_k
        Step 3: if sum_k > sum_j, then update li, ui and sum_j
'''
def maximum_subarray_linear(A:list):
    MSSSF = (0,0,0) #initialize low, high and sum to 0, 0 and 0 respectively
    i:int = 0 #index from beginning of the array
    while i < len(A): # index to end
        l:int = MSSSF[0] #lower_limit_max_sub_arr
        m:int = MSSSF[1] #upper_limit_max_sub_arr
        S:int = MSSSF[2] #sum_max_sub_arr
        assert l <= i
        assert m <= i
        #case1 : the current element by itself is greater than the running sum_max_subarray
        if A[i] >= S:
            l = i
            m = i
            S=A[i]
        #case2: the current elements is contiguous with the current max_subarray
        elif (m == i):
            #extended sum
            _eS_:int = S + A[i] #new sum introduces the currently seen element
            #case2.1: check whether new element extends the max subarray
            k = l # begin from current low and move the low towards i
            _cS_:int = _eS_
            while k <= i:
                if _cS_ > S:
                    S = _cS_
                    l = k
                    m = i
                _cS_ = _cS_ - A[k] # see one less element in the current max subarray contained within l and m
                k += 1
        elif m < i:#this means maximum subarray can be anywhere in between 1 and i
            p = i# index into subarray A[0, i]
            while p >= l: #this looks non-linear because of this inner loop.
                sum:int = A[p]
                q:int = p - 1
                while q>=0:
                    sum += A[q]
                    if sum>S:
                        m = p
                        l = q
                        S=sum
                    q -= 1
                p -= 1
        i += 1
        MSSSF = (l, m, S)
    print(MSSSF)
if __name__ == '__main__':
    maximum_subarray_linear([-2, -5, -1, -7, -21, -30])
    maximum_subarray_linear([-2, -3, 4, -1, -2, 1, 5, -3])
    maximum_subarray_linear([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
