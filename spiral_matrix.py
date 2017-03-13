# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def spiralOrder(self, matrix):
    if not matrix:
      return matrix
    m = len(matrix)
    n = len(matrix[0])
    levels = (min(m, n) + 1) / 2
    res = []
    for i in range(levels):
      res.extend(self._getLevel(matrix, i, m, n))
    return res

  def _getLevel(self, matrix, k, m, n):
    if k == m / 2:
      return [matrix[k][j] for j in range(k, n - k)]
    if k == n / 2:
      return [matrix[i][k] for i in range(k, m - k)]
    top = [matrix[k][j] for j in range(k, n - k - 1)]
    right = [matrix[i][n - k - 1] for i in range(k, m - k - 1)]
    bottom = [matrix[m - k - 1][j] for j in range(n - k - 1, k, -1)]
    left = [matrix[i][k] for i in range(m - k - 1, k , -1)]
    return top + right + bottom + left


if __name__ == '__main__':
  s = Solution()
  m = 5
  n = 3
  matrix = [[n*i+j+1 for j in range(n)] for i in range(m)]
  for row in matrix:
    print row
  print s.spiralOrder(matrix)
