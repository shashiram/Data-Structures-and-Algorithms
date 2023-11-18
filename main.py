"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

    Input: heights = [2,2,5,6,1,3]
    Output: 10
    Explanation: The above is a histogram where width of each bar is 1.
    The largest rectangle is shown in the red area, which has an area = 10 units.

250000000

"""
import math

import test2

heights = [1,2,1,3,4,5,2,1]

for i in range(len(heights)):
    heights[i] = [heights[i], 0, 0]


def fun(i, j):
    if i == j:
        return heights[i][0]
    else:
        mid = math.floor(i + (j - i) / 2)
        left = fun(i, mid)
        right = fun(mid + 1, j)

        maxVal = max(left, right)
        p = mid
        q = mid + 1
        cnt = 0
        loop = 2
        while p >= i and q <= j:

            if heights[p][0] <= heights[q][0] and loop == 2:
                cnt += 1

                if heights[p][0] == heights[q][0]:
                    heights[q][1] = heights[p][1] + heights[p][0] * cnt

                if q == j or heights[p][0] > heights[q + 1][0]:
                    if q < j and heights[p][0] > heights[q + 1][0]:
                        loop = 1
                    heights[p][2] = heights[p][0] * cnt
                    maxVal = max(maxVal, sum(heights[p]))
                    if q == j and i < p:
                        p = p - 1
                        if p >= i and heights[p][0] > heights[p + 1][0]:
                            print(heights[p][0],heights[p + 1][0])

                            break
                    elif q == j and p == i:
                        p = p - 1
                        q = q + 1
                    else:
                        q = q + 1
                else:

                    q = q + 1
            else:
                cnt += 1

                if heights[p][0] == heights[q][0]:
                    heights[p][2] = heights[q][2] + heights[p][0] * cnt

                if p == i or heights[q][0] > heights[p - 1][0]:

                    if p > i and heights[q][0] > heights[p - 1][0]:
                        loop = 2

                    heights[q][1] = heights[q][0] * cnt
                    maxVal = max(maxVal, sum(heights[q]))

                    if p == i and q < j:
                        q = q + 1
                        if q <= j and heights[q - 1] < heights[q]:

                            break
                    elif q == j and p == i:
                        p = p - 1
                        q = q + 1
                    else:
                        p = p - 1
                else:
                    p = p - 1

        return max(maxVal, left, right)


print(fun(0, len(heights) - 1))

for item in heights:
    print(item)
