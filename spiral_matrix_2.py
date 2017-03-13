# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
  """
  >>> solution = Solution()
  """

  def generateMatrix(self, n):
    if n <= 0:
      return []
    matrix = [[0 for j in range(n)] for i in range(n)]

    curr = 1
    for k in range(0, (1 + n) / 2):
      curr = self._fillLevel(matrix, k, n, curr)

    return matrix

  def _fillLevel(self, matrix, k, n, curr):
    if k == n / 2:
      matrix[k][k] = curr
      return

    for j in range(k, n - k -1):
      matrix[k][j] = curr
      curr += 1

    for i in range(k, n - k - 1):
      matrix[i][n - k - 1] = curr
      curr += 1

    for j in range(n - k - 1, k, -1):
      matrix[n - k - 1][j] = curr
      curr += 1

    for i in range(n - k - 1, k, -1):
      matrix[i][k] = curr
      curr +=1

    return curr


if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
  s = Solution()
  for row in s.generateMatrix(3):
    print row
