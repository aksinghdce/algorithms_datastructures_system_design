#!python
# Write a recursive function to get a maximum subarray of an array
# Step 1: Write the program on paper
# Step 2: Manually validate the accuracy of the program with examples
# Step 3: Code the program
# Step 4: Run and Document
import math
def find_maximum_subarray(A:list, low:int, high:int) -> (int, int, int):
    i:int = low
    sum:int = 0
    left_index:int = low
    right_index:int = low
    for i in range(low, high+1, 1):
        sum_:int = 0
        j:int
        for j in range(i, high+1, 1):
            sum_ += A[j]
            if sum_ > sum:
                sum = sum_
                left_index = i
                right_index = j
    return (left_index, right_index, sum)
if __name__ == '__main__':
    #l, r, s = find_maximum_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 0, 15)
    #l, r, s = find_maximum_subarray([-2, -3, 4, -1, -2, 1, 5, -3], 0, 7)
    l, r, s = find_maximum_subarray([2, 5, 1, 7, -21, 30], 0, 5)
    #l, r, s = find_maximum_subarray([-31, -41, 59, 26, -53, 58, 97, -93, -23, 84], 0, 9)
    print("Left_index:",l,"Right_index:",r,"Sum:",s)