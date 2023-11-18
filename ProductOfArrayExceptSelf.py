"""

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Follow up:
    Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""
nums = [1, 2, 3, 4]
ans = []
p = 1
for i in range(len(nums)):
    ans.append(p)
    p = p * nums[i]
p = 1
for i in range(len(nums) - 1, -1, -1):
    if i == 0:
        ans[i] = p
    else:
        ans[i] = ans[i] * p
        p = p * nums[i]