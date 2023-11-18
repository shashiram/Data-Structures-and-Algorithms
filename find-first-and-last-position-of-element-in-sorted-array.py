"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

    Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
"""
import math

nums = [8, 8, 8, 8, 8, 8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8, 10, 10]
target = 10


def fun(i, j):
    print(i,j)
    if i == j:
        rt = [-1, -1]
        if nums[i] == target:
            if i == 0 or ((i - 1) >= 0 and nums[i - 1] != nums[i]):
                rt[0] = i
            if i == len(nums) - 1 or ((i + 1) <= len(nums) - 1 and nums[i + 1] != nums[i]):
                rt[1] = i
        return rt
    elif nums[i] == nums[j]:
        rt = [-1, -1]
        if nums[i]==target:
            if i==0 or ((i - 1) >= 0 and nums[i - 1] != nums[i]):
                rt[0]=i
            if j == len(nums) - 1 or ((j + 1) <= len(nums) - 1 and nums[j + 1] != nums[j]):
                rt[1] = j
        return rt
    else:
        mid = math.floor(i + (j - i) / 2)
        if target < nums[mid]:
            return fun(i, mid)
        elif target > nums[mid]:
            return fun(mid + 1, j)
        else:
            left = fun(i, mid)
            right = fun(mid + 1, j)
            return [max(left[0], right[0]), max(left[1], right[1])]


print(fun(0, len(nums) - 1))
