# Problem url.

class Solution(object):
  """
  """

  def rotate(self, matrix):
    n = len(matrix)
    for i in range(n/2):
      self._rotateLevel(matrix, i, n)
    

  def _rotateLevel(self, matrix, i, n):
    """Rotate level i."""
    j = 0
    while j < n - i * 2 - 1:
      self._rotateCell(matrix, i, j, n)
      j += 1

  def _rotateCell(self, matrix, i, j, n):
    start = i
    end = n - i - 1
    top = matrix[start][start+j]
    matrix[start][start+j] = matrix[end-j][start]  # Top from left.
    matrix[end-j][start] = matrix[end][end-j]  # Left from bottom.
    matrix[end][end-j] = matrix[start+j][end]  # Bottom from right.
    matrix[start+j][end] = top  # Right from top.
    



if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
  solution = Solution()
  # matrix = [[1, 2], [3, 4]] 
  # solution.rotate(matrix)
  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
  solution.rotate(matrix)
  print matrix

