# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def isValidSudoku(self, board):
    if not board:
      return False
    if len(board) != 9:
      return False
    for row in board:
      if not row or len(row) != 9:
        return False

    n = 9
    for i in range(n):
      if not self._IsValid(board[i]):
        return False
        

    for j in range(n):
      if not self._IsValid([row[j] for row in board]):
        return False

    for i in range(0, n, 3):
      for j in range(0, n, 3):
        if not self._IsValid(
            [
                board[i+l][j+k] for k in range(3) for l in range(3)
            ]
        ):
          return False
    return True
  def _IsValid(self, values):
    num_set = set()
    for v in values:
      if v == '.':
        continue
      elif v <= '9' and v >= '1':
        if v in num_set:
          return False
        else:
          num_set.add(v)
      else:
        return False
    return True


if __name__ == '__main__':
  import doctest
  doctest.testmod()
