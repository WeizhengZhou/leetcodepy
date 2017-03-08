# https://leetcode.com/problems/combination-sum/?tab=Description
#
# Given a set of candidate numbers (C) (without duplicates) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]


class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.combinationSum([2, 3, 6, 7], 7)
  [[7], [2, 2, 3]]
  """

  def combinationSum(self, candidates, target):
    if not candidates:
      return []
    return self._buildSolutions(candidates, target, [], 0)

  def _buildSolutions(self, candidates, target, solution, index):
    if target < 0:
      return []
    if target == 0:
      return [solution,]
    if index >= len(candidates):
      return []
    all_solutions = []
    all_solutions.extend(
      self._buildSolutions(
          candidates, target, solution, index + 1)
    )
    new_solution = solution[:]
    while target > 0:
      target -= candidates[index]
      new_solution = new_solution[:] + [candidates[index],]
      all_solutions.extend(
          self._buildSolutions(
              candidates, target, new_solution, index + 1
          )
      )
    return all_solutions


if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
  solution = Solution()
  print solution.combinationSum([2, 3,], 7)
