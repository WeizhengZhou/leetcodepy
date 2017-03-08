# https://leetcode.com/problems/combination-sum-ii/?tab=Description
#
# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

import collections


class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.combinationSum2([1, 1, 6], 7)
  [[1,6]]
  """

  def combinationSum2(self, candidates, target):
    if not candidates:
      return []
    candidates.sort()
    self.candidates = candidates
    self.counter = collections.Counter(candidates)
    return self._combinationSum2(target, [], 0)

  def _combinationSum2(self, target, solution, index):
    if target < 0:
      return []
    if target == 0:
      return [solution,]
    if index > len(self.candidates) - 1:
      return []

    solutions = []
    curr_candidate = self.candidates[index]
    curr_count = self.counter.get(curr_candidate)
    next_index = index + curr_count
    for i in range(curr_count + 1):
      new_solution = solution + [curr_candidate,] * i
      solutions.extend(
          self._combinationSum2(
              target - i * curr_candidate, new_solution, next_index)
      )
    return solutions


if __name__ == '__main__':
  solution = Solution()
  print solution.combinationSum2([1, 1, 6], 7)
