"""

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

"""

given = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
row=len(given)
col=len(given[0])

memo={}

def dp(i,j):

    key=hash((i,j))
    if key in memo:
        return memo[key]


    list=[]

    if isValid(i-1,j) and given[i][j]<given[i-1][j]:
        path=1+dp(i-1,j)
        list.append(path)
    if isValid(i+1,j) and given[i][j]<given[i+1][j]:
        path=1+dp(i+1,j)
        list.append(path)
    if isValid(i,j-1) and given[i][j]<given[i][j-1]:
        path=1+dp(i,j-1)
        list.append(path)
    if isValid(i,j+1) and given[i][j]<given[i][j+1]:
        path=1+dp(i,j+1)
        list.append(path)
    
    if len(list)==0:
        memo[key]=1
        return 1
    else:
        max_val=max(list)
        memo[key]=max_val
        return max_val

def isValid(i,j):
    return (i>=0 and i<row ) and (j>=0 and j<col )




max_val=0
for i in range(row):
    for j in range(col):

        val=dp(i,j)
        print(given[i][j],val)
        max_val=max(val,max_val)

print(max_val)












