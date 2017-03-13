# https://leetcode.com/problems/jump-game-ii/?tab=Description

import sys


class Solution(object):
  """
  >>> solution = Solution()
  """

  # def jump(self, nums):

  #   if not nums or len(nums) == 1:
  #     return 0
  #   MAX_STEP = sys.maxsize
  #   n = len(nums)

  #   steps = [MAX_STEP,] * n
  #   steps[-1] = 0

  #   i = n - 2
  #   while i  >= 0:
  #     if nums[i] + i >= n:
  #       steps[i] = 1
  #       i -= 1
  #       continue
  #     j = i + 1
  #     while j < min(i + nums[i] + 1, n):
  #       steps[i] = min(steps[i], steps[j])
  #       j += 1
  #     steps[i] += 1
  #     i -= 1
  #   return steps[0]
        
  def jump(self, nums):
    if not nums:
      return 0
    curr_level = [0,]
    step = 0
    while curr_level:
      next_level = set()
      print curr_level
      for i in curr_level:
        if i + nums[i] >= len(nums):
          return step
        for j in range(nums[i] + 1):
          next_level.add(i + j)
      curr_level = next_level
      step += 1
    return step


if __name__ == '__main__':
  s = Solution()
  print s.jump([1,2,0,1])
  print s.jump([[2,3,1,1,4]])
  # import doctest
  # doctest.testmod()
