# https://leetcode.com/problems/3sum/?tab=Description


class Solution(object):
  """
  >>> Solution().threeSum([-1, 0, 1])
  [[-1, 0, 1]]
  >>> Solution().threeSum([-1, 0, 1, 2, -1, -4])
  [[-1, 0, 1], [-1, -1, 2]]
  """

  def threeSum(self, numbers):
    if not numbers: 
      return []
    if len(numbers) < 3:
      return []
    numbers.sort()
    solutions = list()
    i = 0
    while i < len(numbers):
      l = i + 1  # Left index.
      r = len(numbers) - 1  # Right index
      while l < r:
        three_sum = numbers[i] + numbers[l] + numbers[r]
        if three_sum == 0:
          solutions.append([numbers[i], numbers[l], numbers[r]])
          l = self._skipDuplicates(l, numbers)
        elif three_sum < 0:
          l += 1
        else: 
          r -= 1
      i = self._skipDuplicates(i, numbers)
    return solutions

  def _skipDuplicates(self, index, numbers):
    curr = index + 1
    while curr < len(numbers) and numbers[curr] == numbers[index]:
      curr += 1
    return curr


if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
