# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Subscribe to see which companies asked this question.


# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def minPathSum(self, grid):

    if not grid or not grid[0]:
      return 0

    m = len(grid)
    n = len(grid[0])
    dp = [[0 for j in range(n)] for i in range(m)]
    dp[0][0] = grid[0][0]

    for i in range(1, m):
      dp[i][0] = dp[i-1][0] + grid[i][0]

    for j in range(1, n):
      dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, m):
      for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]



if __name__ == '__main__':
  import doctest
  doctest.testmod()
