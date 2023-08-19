https://leetcode.com/problems/squares-of-a-sorted-array/

Solution Steps:
Two Pointers Initialization: Initialize two pointers, left at the beginning of the array and right at the end of the array.
Create a Result Array: This array will store the squares of the numbers in non-decreasing order. Its index will start from the end and move towards the beginning.
Compare and Place: Compare the absolute values of the elements at left and right. The larger absolute value will give the larger square. Place the square of the larger absolute value at the current index of the result array and decrement that index. Then, move the pointer (either left or right) which had the larger absolute value.
Repeat: Continue this process until all elements of the nums array have been squared and placed in the result array.

def sortedSquares(nums):
    n = len(nums)
    # Initialize the result array and pointers
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1  # Start from the end of the result array

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        # Place the larger square at the current index of result
        if left_square > right_square:
            result[index] = left_square
            left += 1
        else:
            result[index] = right_square
            right -= 1

        index -= 1

    return result
Time Complexity:
The solution iterates through the list once, so the time complexity is O(n)

Space Complexity:
The space complexity is O(n)
