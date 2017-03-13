# https://leetcode.com/problems/n-queens/?tab=Description

import collections 


class Solution(object):
  """
  >>> solution = Solution()
  """

  def solveNQueens(self, n):
    solutions = []
    board = [['.' for j in range(n)] for i in range(n)]
    self._placeRow(n, board, 0, solutions)
    return solutions

  def _placeRow(self, n, board, i, solutions):
    # print i, board
    if i == n:
      solutions.append([''.join(row[:]) for row in board])
      return
    for j in range(n):
      board[i][j] = 'Q'
      if self._isValidPlacement(n, board, i, j):
        self._placeRow(n, board, i + 1, solutions)
      board[i][j] = '.'

  def _isValidPlacement(self, n, board, i, j):
    return (
        self._isValid(board[i]) and
        self._isValid([row[j] for row in board]) and 
        self._isValidDiagonal(board, i, j, n) 
    )

  def _isValid(self, elements):
    counter = collections.Counter(elements)
    if counter.get('Q') > 1:
      return False
    return True

  def _isValidDiagonal(self, board, i, j, n): 
    ii, jj = i + 1, j + 1 
    while self._inRange(ii, jj, n):
      if board[ii][jj] == 'Q':
        return False
      ii += 1
      jj += 1

    ii, jj = i + 1, j - 1 
    while self._inRange(ii, jj, n):
      if board[ii][jj] == 'Q':
        return False
      ii += 1
      jj -= 1

    ii, jj = i - 1, j + 1 
    while self._inRange(ii, jj, n):
      if board[ii][jj] == 'Q':
        return False
      ii -= 1
      jj += 1
    
    ii, jj = i - 1, j - 1 
    while self._inRange(ii, jj, n):
      if board[ii][jj] == 'Q':
        return False
      ii -= 1
      jj -= 1

    return True

  def _inRange(self, i, j, n):
    return i >= 0 and j >= 0 and i < n and j < n


if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
  s = Solution()
  solutions = s.solveNQueens(4)
  for solution in solutions:
    print solution
