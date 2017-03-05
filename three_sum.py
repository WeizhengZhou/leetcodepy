# https://leetcode.com/problems/3sum/?tab=Description

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

    index_by_number = {
        numbers[i]: i for i in range(len(numbers))
    }
    solutions = []
    seen_solution_set = set()
    for i in range(len(numbers) - 2):
      for j in range(i+1, len(numbers) - 1):
        two_sum = numbers[i] + numbers[j]
        third_index = index_by_number.get(-two_sum, None)
        if third_index and third_index not in [i, j]:
          # print i, j, third_index
          solution = sorted([numbers[i], numbers[j], numbers[third_index]])
          if tuple(solution) not in seen_solution_set:
            solutions.append(solution)
            seen_solution_set.add(tuple(solution))
    return solutions
    

if __name__ == '__main__':
  print Solution().threeSum([-1, 0, 1, 2, -1, -4])
  # import doctest
  # doctest.testmod()
