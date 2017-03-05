# https://leetcode.com/problems/3sum/?tab=Description

import collections


class Solution(object):
  """
  >>> Solution().threeSum([-1, 0, 1])
  [[-1, 0, 1]]
  >>> Solution().threeSum([-1, 0, 1, 2, -1, -4])
  [[-1, 0, 1], [-1, -1, 2]]
  """

  def threeSum(self, numbers):
    if not numbers or len(numbers) < 3:
      return []

    index_by_number = collections.defaultdict(list)

    for i in range(len(numbers)):
      index_by_number[numbers[i]].append(i)

    solutions = []
    seen_solution_set = set()
    for i in range(len(numbers) - 2):
      for j in range(i+1, len(numbers) - 1):
        two_sum = numbers[i] + numbers[j]
        third_indices = index_by_number.get(-two_sum)

        third_index = self._findThirdIndex(third_indices, i, j)
        if third_index:
          solution = sorted([numbers[i], numbers[j], numbers[third_index]])
          if tuple(solution) not in seen_solution_set:
            solutions.append(solution)
            seen_solution_set.add(tuple(solution))
    return solutions

  def _findThirdIndex(self, third_indices, i, j):
    if not third_indices:
      return None
    elif len(third_indices) == 1 and third_indices[0] > j:
      return third_indices[0]
    elif len(third_indices) == 2 and third_indices[1] > j:
      return third_indices[1]
    elif len(third_indices) > 2:
      return third_indices[2]
    return None
    

if __name__ == '__main__':
  # print Solution().threeSum([-1, 0, 1, 2, -1, -4])
  import doctest
  doctest.testmod()
