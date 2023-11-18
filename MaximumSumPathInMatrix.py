""" 

Given an n*m matrix, the task is to find the maximum sum of elements of cells starting from the cell (0, 0) to cell (n-1, m-1). 
However, the allowed moves are right, downwards or diagonally right, i.e, from location (i, j) next move can be (i+1, j), or, (i, j+1), or (i+1, j+1). Find the maximum sum of elements
satisfying the allowed moves.

Input:
mat[][] = {{100, -350, -200},
           {-100, -300, 700}}
Output: 500
Explanation: 
Path followed is 100 -> -300 -> 700

alg:

 dp(i,j)= max(dp(i,j+1),dp(i+1,j),dp(i+1,j+1))

 """

given = [[100, -350, -200],
         [-100, -300, 700]]

row = len(given)
col = len(given[0])

memo = {}


def dp(i, j):
    key = str(i) + "-" + str(j)
    if key in memo:
        print(key)
        return memo.get(key)

    if i == row and j == col:
        memo[key] = 0
        return 0

    if i < row and j < col:
        cn = max(given[i][j] + dp(i, j + 1), given[i][j] + dp(i + 1, j), given[i][j] + dp(i + 1, j + 1))
        memo[key] = cn
        return cn
    else:
        memo[key] = 0
        return 0


print(dp(0, 0))
print(memo)
