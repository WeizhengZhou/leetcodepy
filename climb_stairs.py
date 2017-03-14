# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.


# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def climbStairs(self, n):
    if n <= 0:
      return 0
    if n == 1:
      return 1
    if n == 2:
      return 2

    dp = [0 for i in range(n)]
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
      dp[i] += (dp[i-1] + dp[i-2])
    return dp[-1]


if __name__ == '__main__':
  import doctest
  doctest.testmod()
