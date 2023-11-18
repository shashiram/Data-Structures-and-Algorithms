"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

    Input: arr = [4,2,3,0,3,1,2], start = 5
    Output: true
    Explanation: 
    All possible ways to reach at index 3 with value 0 are: 
    index 5 -> index 4 -> index 1 -> index 3 
    index 5 -> index 6 -> index 4 -> index 1 -> index 3 


"""
arr = [3,0,2,1,2]
n=len(arr)


visited={}

def dp(i):


    if (i in visited ) or (i<0 or i>=n):
        return False

    if arr[i]==0:
        visited[i]=True
        return True
    else:
        visited[i]=True
        return dp(i+arr[i]) or dp(i-arr[i])
    
print(dp(2))


            




