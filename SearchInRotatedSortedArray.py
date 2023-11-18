"""
nums1=[0,1,2,3,4,5,6,7] =>
index 2 => k
t=3

leftlen=(k)

nums1[k+p]=
nums1[k]=2=nums[0]

[2,3,4,5,6,7,0,1]

nums[n-1]=nums1[k-1]
nums[0]=nums1[k]


 [2,3,4,5]    [6,7,0,1]

[2,3] [4,5]  [6,7] [0,1]

l1 + l2 =n
k-0

"""
import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def rotatedSearch(i, j):
            if i > j:
                return -1
            if target == nums[i]:
                return i
            if target == nums[j]:
                return j
            if i + 1 == j:
                return -1
            mid = math.floor(i + (j - i) / 2)
            if target == nums[mid]:
                return mid
            else:
                if nums[i] < nums[mid]:
                    if nums[i] < target < nums[mid]:
                        return rotatedSearch(i + 1, mid - 1)
                    else:
                        return rotatedSearch(mid + 1, j - 1)
                else:
                    if nums[mid] < target < nums[j]:
                        return rotatedSearch(mid + 1, j - 1)
                    else:
                        return rotatedSearch(i + 1, mid - 1)

        return rotatedSearch(0, len(nums) - 1)


sl = Solution()
nums = [5,1,2,3,4]
print(sl.search(nums, 1))
