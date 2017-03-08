# https://leetcode.com/problems/sudoku-solver/?tab=Description

class Solution(object):
  """
  >>> solution = Solution()
  >>> s = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
  >>> solution.solveSudoku([list(i) for i in s])
  """

  def solveSudoku(self, board):
    self._solve(board, 0, 0)


  def _solve(self, board, i, j):
    if i >= 9:
      return True
    if j >= 9:
      return self._solve(board, i+1, 0)

    if board[i][j] != '.':
      return self._solve(board, i, j+1)

    # Try all solutions.
    for k in range(1, 10):
      board[i][j] = str(k)
      if self._isChangeValid(board, i, j):
        # print i, j
        # self._printBoard(board)
        if self._solve(board, i, j+1):
          return True
    # Rollback.
    board[i][j] = '.'
    return False

  def _isChangeValid(self, board, i, j):
    if not self._isValid([row[j] for row in board]):
      return False

    if not self._isValid(board[i]):
      return False

    start_i = (i / 3) * 3
    start_j = (j / 3) * 3
    cubic = [board[start_i + k][start_j + l] for l in range(0, 3) for k in range(0, 3)]
    if not self._isValid(cubic):
      return False
    return True


  def _isValid(self, data):
    num_set = set()
    for d in data:
      if d == '.':
        continue
      if d in num_set:
        return False
      num_set.add(d)
    return True

  def _printBoard(self, board):
    for row in board:
      print row


if __name__ == '__main__':
  import doctest
  doctest.testmod()
  solution = Solution()
  s = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
  # board = [list(i) for i in s]
  # solution.solveSudoku(board)
