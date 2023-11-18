"""
Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

    Example 1:

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
"""

nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]

queue = []
q = 0

for i in range(len(nums)):
    if nums[i] == 0:
        queue.append(i)
    else:
        if len(queue) != 0:
            nums[queue[q]] = nums[i]
            nums[i] = 0
            queue.append(i)
            q += 1
print(nums)
