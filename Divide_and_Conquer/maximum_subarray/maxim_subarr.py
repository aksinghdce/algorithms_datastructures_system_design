# Write a recursive function to get a maximum subarray of an array
# Step 1: Write the program on paper
# Step 2: Manually validate the accuracy of the program with examples
# Step 3: Code the program
# Step 4: Run and Document
import math
def find_max_crossing_subarray(A:list, low:int, mid:int, high:int):
    left_sum: int = -1000000
    max_left: int = -1
    suml: int = 0
    i:int
    for i in range(mid, low - 1, -1):
        suml += suml + A[i]
        if suml > left_sum:
            left_sum = suml
            max_left = i
    right_sum:int = -1000000
    max_right:int = mid+1
    sum:int = 0
    j:int
    for j in range(mid+1, high+1, 1):
        sum += sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum+right_sum)

def find_maximum_subarray(A:list, low:int, high:int):
    if low == high:
        return (low, high, A[low])
    mid:int = math.floor((low + high)/2)
    left_low:int
    left_high:int
    left_sum:int
    left_low,left_high,left_sum = find_maximum_subarray(A, low, mid)
    if left_low == low and left_high == mid:
        print("left_max", left_low, left_high, left_sum)
    right_low:int
    right_high:int
    right_sum:int
    right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
    if right_low == (mid+1) and right_high == high:
        print("right_max", right_low, right_high, right_sum)
    mid_low:int
    mid_high:int
    mid_sum:int
    mid_low, mid_high, mid_sum = find_max_crossing_subarray(A, low, mid, high)
    if mid_low == low and mid_high == high:
        print("cross_max", mid_low, mid_high, mid_sum)
    if left_sum>= right_sum and left_sum >= mid_sum:
        return (left_low, left_high, left_sum)
    elif right_sum>=left_sum and right_sum>=mid_sum:
        return (right_low, right_high, right_sum)
    else:
        return (mid_low, mid_high, mid_sum)
if __name__ == '__main__':
    #l, r, s = find_maximum_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 0, 15)
    l, r, s = find_maximum_subarray([-2, -3, 4, -1, -2, 1, 5, -3], 0, 7)
    print("Left_index:",l,"Right_index:",r,"Sum:",s)