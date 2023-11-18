"""
You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].

For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.

An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].

Example 1:

    Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
    Output: 1
    Explanation:
    Swap nums1[3] and nums2[3]. Then the sequences are:
    nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
    which are both strictly increasing.

"""
nums1 = [2, 1, 6, 7, 8, 13, 15, 11, 18, 13, 20, 24, 17, 28, 22, 23, 36, 37, 39, 34, 43, 38, 48, 41, 46, 48, 49, 50, 56,
         55, 59, 60, 62, 64, 66, 75, 69, 70, 71, 74, 87, 78, 95, 97, 81, 99, 85, 101, 90, 91, 93, 95, 107, 109, 101,
         111, 106, 114, 115, 117, 118, 115, 121, 122, 123, 124, 125, 126, 134, 131, 133, 136, 142, 149, 151, 152, 145,
         156, 158, 150, 162, 159, 161, 165, 169, 170, 169, 174, 172, 176, 177, 181, 183, 192, 186, 188, 189, 196, 198,
         200]
nums2 = [0, 4, 10, 11, 12, 9, 10, 16, 12, 19, 15, 16, 25, 20, 33, 34, 27, 29, 32, 40, 35, 45, 40, 50, 51, 52, 53, 55,
         52, 58, 58, 61, 62, 66, 71, 68, 78, 81, 83, 84, 75, 91, 79, 80, 98, 83, 100, 89, 102, 103, 105, 106, 96, 98,
         110, 105, 113, 109, 110, 111, 112, 120, 116, 118, 126, 130, 131, 133, 129, 137, 138, 140, 137, 138, 140, 142,
         154, 147, 149, 159, 152, 163, 164, 163, 166, 168, 171, 170, 175, 176, 177, 181, 186, 184, 193, 194, 195, 190,
         195, 200]
memo = {}
leftMemo = {}


def dp(i):
    if i in memo:
        print(i)
        return memo[i]
    if i >= len(nums1) - 1:
        return 0
    if i == len(nums1) - 2:
        if nums1[i] >= nums1[i + 1] or nums2[i] >= nums2[i + 1]:
            return 1
        return 0
    if nums1[i] >= nums1[i + 1] or nums2[i] >= nums2[i + 1]:
        leftMemo[i] = leftSwap(i)
        rightSwaps = rightSwap(i + 1)
        memo[i] = min(leftMemo[i] + dp(rightSwaps + i), rightSwaps + dp(rightSwaps + i + 1))
        return memo[i]
    else:
        memo[i] = dp(i + 1)
        return memo[i]


def rightSwap(i):
    cnt = 1
    while (i + 1) < len(nums1) and (nums1[i] >= nums2[i + 1] or nums2[i] >= nums1[i + 1]):
        cnt = cnt + 1
        i += 1
    return cnt


def leftSwap(i):
    cnt = 1
    flag = True
    while flag:
        if (i - 1) >= 0 and (i - 1) in leftMemo:
            cnt += 1 + leftMemo[(i - 1)]
            break
        if (i - 1) >= 0 and (nums1[i - 1] >= nums2[i] or nums2[i - 1] >= nums1[i]):
            cnt += 1
            i = i - 1
        else:
            flag = False
    return cnt


print(dp(0))
