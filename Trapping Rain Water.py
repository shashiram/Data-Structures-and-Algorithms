"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Ex:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
    In this case, 6 units of rain water (blue section) are being trapped.

[4, 2, 0, 3, 2, 5]

4*(4)=16

16-7=9

(2-1)-1

[[(1, 1), (2, 3)], [(2, 3), (3, 7)], [(3, 7), (2, 10)]]

area:
  h=min(a,b)
  l=j-i -1
  ar=h*l


  [0, 1, 2, 0, 3, 0, 1, 2, 0, 0, 4, 2, 1, 2, 5, 0, 1, 2, 0, 2]

  [2,3]=> [3,4]=> [4,5]=> [5,2]=> [2,2]

  2+ 12 +7+3+2


"""
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        def fun(i):
            hgtPoint = None
            lowestPoint = False
            lowestPointNum = None
            if height[i - 1] < height[i]:
                maxPoint = None
            else:
                maxPoint = (height[i - 1], (i - 1))
            intervals = []
            while i < len(height):
                if (i == len(height) - 1) or (height[i - 1] < height[i] > height[i + 1]) or (
                        (hgtPoint is not None) and (height[i - 1] <= height[i] > height[i + 1])
                ):

                    if lowestPoint:
                        if maxPoint is None:
                            tempList = []
                            tempList.append((maxPoint[0], maxPoint[1]))
                            tempList.append((height[i], i))
                            intervals.append(tempList)
                        else:
                            if (len(intervals) == 0) or (maxPoint[0] > intervals[-1][1][0] < height[i]):

                                pointer=len(intervals)-1
                                while pointer>=0 and (intervals[pointer][1][0]<height[i]):
                                    intervals.pop()
                                    pointer=pointer-1

                                tempList = []
                                if len(intervals)==0:
                                    tempList.append((maxPoint[0], maxPoint[1]))
                                else:
                                    tempList.append(intervals[-1][1])
                                tempList.append((height[i], i))

                                intervals.append(tempList)
                                if maxPoint[0] <= height[i]:
                                    break
                            else:
                                tempList = []
                                tempList.append(intervals[-1][1])
                                tempList.append((height[i], i))
                                intervals.append(tempList)
                        lowestPoint = False
                        if maxPoint[0] <= height[i]:
                            maxPoint = (height[i], i)

                    else:
                        maxPoint = (height[i], i)
                    if height[i - 1] == height[i]:
                        hgtPoint = None

                if (i < len(height) - 1) and (height[i - 1] < height[i] >= height[i + 1]):
                    if height[i] == height[i + 1]:
                        hgtPoint = height[i]

                if (i < len(height) - 1) and (height[i - 1] > height[i] <= height[i + 1]):
                    if height[i] == height[i + 1]:
                        lowestPointNum = height[i]
                    else:
                        lowestPoint = True
                if (i < len(height) - 1) and (lowestPointNum is not None) and (
                        lowestPointNum == height[i] < height[i + 1]):
                    lowestPoint = True
                    lowestPointNum = None
                if (i < len(height) - 1) and (lowestPointNum is not None) and (
                        lowestPointNum == height[i] > height[i + 1]):
                    lowestPointNum = None
                i += 1
            print(intervals)
            return intervals, (i + 1)

        if len(height) == 1 or len(height) == 2:
            return 0
        intervalsList = []
        p = 1
        while p < len(height):
            pair = fun(p)
            if len(pair[0]) != 0:
                intervalsList.append(pair[0])
            p = pair[1]

        total = 0
        for intervals in intervalsList:
            for i in range(len(intervals)):
                interval = intervals[i]
                h = min(interval[0][0], interval[1][0])
                l = (interval[1][1] - interval[0][1]) - 1
                area = h * l
                sum = 0
                p = interval[0][1] + 1
                while p < interval[1][1]:
                    sum = sum + (height[p] if height[p] <= h else h)
                    p += 1
                total = total + (area - sum)

        return total


sl = Solution()
height = [0,1,0,0,4,4,8,9,2,8,7,5,3,3,0,1,8,9,5,7,9,0,8,3,0]
print(sl.trap(height))
