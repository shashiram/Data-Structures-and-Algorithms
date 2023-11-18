""" Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array. 


Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.



"""
str1='ram'
digit_str=''
m=3
for i in range(len(str1)):
    digit_str=digit_str+str(ord(str1[i]))

print(digit_str)

def fun_hash(h_str):
    return int(h_str) % m

print(fun_hash(digit_str))

            














