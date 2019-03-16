def maximum_subarray_linear2(A:list):
    max_sum:int = -10000
    max_low:int = -1
    max_high:int = -1
    curr_sum:int = -10000
    i:int = 0
    while i < len(A):
        if curr_sum >= 0:
            curr_sum += A[i]
        else:
            curr_sum = A[i]
            if curr_sum > 0: #as soon as my current sum recovers to become positive, i reset max_low
                max_low = i
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_high = i
        i += 1
    return (max_low, max_high, max_sum)

if __name__ == '__main__':
    print(maximum_subarray_linear2([-2, -5, -1, -7, -21, -30]))
    print(maximum_subarray_linear2([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(maximum_subarray_linear2([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))