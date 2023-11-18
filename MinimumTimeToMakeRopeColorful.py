"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

    ex :
        Input: colors = "abaac", neededTime = [1,2,3,4,5]
        Output: 3
        Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
        Bob can remove the blue balloon at index 2. This takes 3 seconds.
        There are no longer two consecutive balloons of the same color. Total time = 3.

"""
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        totalTime = 0
        i = 0
        while (i + 1) < len(colors):
            if colors[i] == colors[i + 1]:
                j = i + 1
                maxTime = neededTime[i]
                sum = neededTime[i]
                while j < len(colors) and colors[i] == colors[j]:
                    if neededTime[j] > maxTime:
                        maxTime = neededTime[j]
                    sum = sum + neededTime[j]
                    j = j + 1
                totalTime = totalTime + (sum - maxTime)
                i = j
            else:
                i += 1
        return totalTime


colors = "bbbaaa"
neededTime = [4, 9, 3, 8, 8, 9]
sl = Solution()
print(sl.minCost(colors, neededTime))

