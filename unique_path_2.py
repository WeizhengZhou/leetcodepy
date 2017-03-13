# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.


# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def uniquePathsWithObstacles(self, grid):
    if not grid:
      return 0
    m = len(grid)
    n = len(grid[0])

    dp = [[0 for j in range(n)] for i in range(m)]
    dp[0][0] = 1
    for j in range(1, n):
      if grid[0][j]:
        dp[0][j] = 0
      else:
        dp[0][j] = dp[0][j-1]

    for i in range(1, m):
      if grid[i][0]:
        dp[i][0] = 0
      else:
        dp[i][0] = dp[i-1][0]

    for i in range(1, m):
      for j in range(1, n):
        if grid[i][j]:
          dp[i][j] = 0
        else:
          dp[i][j] += (dp[i-1][j] + dp[i][j-1])
    return dp[m-1][n-1]


if __name__ == '__main__':
  import doctest
  doctest.testmod()
