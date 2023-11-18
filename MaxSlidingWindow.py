"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
nums = [1,3,-1,4,5], k = 3

[3,1,-1,4,5] => [3,4,-1,4,5]

[0]=0
[1]=1
[2]=2

idx=0 => 1
left=1 => 3

idx=0 => 3
left=1 => 1

ha[0]=1
ha[1]=0
ha[3]=1




"""
import math
from typing import List

import test2


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]

        handleByOrgId = {}
        handleByCurId = {}

        def heapDown(idx):
            left = 2 * idx + 1
            right = 2 * idx + 2
            maxIdx = idx

            if not (left >= k and right >= k):
                if left < k and nums[maxIdx] < nums[left]:
                    maxIdx = left
                if right < k and nums[maxIdx] < nums[right]:
                    maxIdx = right
                if maxIdx != idx:
                    temp = nums[idx]
                    nums[idx] = nums[maxIdx]
                    nums[maxIdx] = temp

                    orgIdForIdx = handleByCurId[idx]
                    handleByOrgId[orgIdForIdx] = maxIdx

                    orgIdForMaxId = handleByCurId[maxIdx]
                    handleByOrgId[orgIdForMaxId] = idx

                    handleByCurId[idx] = orgIdForMaxId
                    handleByCurId[maxIdx] = orgIdForIdx

                    heapDown(maxIdx)

        def heapUp(idx):
            while ((idx - 1) / 2) >= 1 and idx > 1:
                parent = math.floor((idx - 1) / 2)
                if nums[parent] < nums[idx]:
                    temp = nums[idx]
                    nums[idx] = nums[parent]
                    nums[parent] = temp

                    orgIdForIdx = handleByCurId[idx]
                    handleByOrgId[orgIdForIdx] = parent

                    orgIdForParent = handleByCurId[parent]
                    handleByOrgId[orgIdForParent] = idx

                    handleByCurId[idx] = orgIdForParent
                    handleByCurId[parent] = orgIdForIdx
                    idx = parent
                else:
                    break

        def heapUpOrDown(idx):
            parent = math.floor((idx - 1) / 2)
            if parent >= 1 and nums[parent] < nums[idx]:
                heapUp(idx)
            else:
                heapDown(idx)

        def heapify():
            j = k
            while j > 0:
                heapDown(j)
                j -= 1

        firstMaxVal = 0
        i = 0
        while i < k:
            if i != 0:
                handleByOrgId[i] = i
                handleByCurId[i] = i
            firstMaxVal = max(firstMaxVal, nums[i])
            i += 1

        returnList = [firstMaxVal]
        handleByOrgId[k] = k
        handleByCurId[k] = k
        heapify()

        p = k + 1
        q = 1
        while p < len(nums):
            returnList.append(nums[1])
            updateIdx = handleByOrgId[q]

            q = q + 1
            nums[updateIdx] = nums[p]
            handleByOrgId[p] = updateIdx
            handleByCurId[updateIdx] = p
            heapUpOrDown(updateIdx)
            p = p + 1

        returnList.append(nums[1])
        return returnList


nums = [1,3,-1,-3,5,3,6,7]
k =3
sl = Solution()
print(sl.maxSlidingWindow(nums, k))
