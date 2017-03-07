# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.longestValidParentheses(')()())')
  4
  """

  def longestValidParentheses(self, s):
    # l[i, j] = l[i+1, j-1] and l[i] == '(' and l[j] == ')'
    if not s or len(s) == 1:
      return 0
    n = len(s)
    matrix = [
        [False for j in range(n)]
        for i in range(n)
    ]
    for i in range(1, n):
      matrix[i][i-1] = True

    res = 0
    for k in range(2, n):
      for i in range(0, n-k):
        j = i + k - 1 
        matrix[i][j] = matrix[i+1][j-1] and s[i] == '(' and s[j] == ')'
        if matrix[i][j]:
          res = max(res, j-i+1)

    return res



if __name__ == '__main__':
  import doctest
  doctest.testmod()
