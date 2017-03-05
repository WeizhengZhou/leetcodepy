# https://leetcode.com/problems/3sum-closest/?tab=Description


class Solution(object):
  """
  >>> Solution().threeSumClosest([-1, 2, 1, -4], 1)
  2
  """

  def threeSumClosest(self, nums, target):
    if not nums or len(nums) < 3:
      return 0
    nums.sort()
    n = len(nums)
    i = 0
    closest = None
    while i < n:
      l = i + 1
      r = n - 1
      while l < r:
        three_sum = nums[i] + nums[l] + nums[r]
        if closest == None:
          closest = three_sum
        if abs(three_sum - target) < abs(closest - target):
          closest = three_sum
        if three_sum == target:
          return target
        elif three_sum < target:
          l += 1
        else: 
          r -= 1
      i += 1
    return closest


if __name__ == '__main__':
  # print Solution().threeSumClosest([0, 0, 0], 1)
  import doctest
  doctest.testmod()
