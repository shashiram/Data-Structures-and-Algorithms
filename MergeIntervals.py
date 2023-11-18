"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        n = len(intervals)
        rt = []
        pre = intervals[0]
        i = 1
        while i < len(intervals):
            if pre[1] < intervals[i][0]:
                rt.append(pre)
                if i == n - 1:
                    rt.append(intervals[i])
                    break
                pre = intervals[i]
            elif intervals[i][0] <= pre[1] <= intervals[i][1]:
                if i == n - 1:
                    rt.append([pre[0], intervals[i][1]])
                    break
                pre = [pre[0], intervals[i][1]]
            else:
                if i == n - 1:
                    rt.append(pre)
                    break
            i += 1

        return rt
