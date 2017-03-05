# https://leetcode.com/problems/container-with-most-water/?tab=Description

class Solution(object):
  """
  >>> Solution().maxArea([1, 2, 3])
  2
  >>> Solution().maxArea([1,])
  0
  >>> Solution().maxArea([2, 1, 5, 3])
  6
  """

  def maxArea(self, heights):
    if not heights or len(heights) == 1:
      return 0

    left = 0
    right = len(heights) - 1

    max_area = 0
    while left < right:
      height = min(heights[left], heights[right])
      width = right - left
      max_area = max(max_area, height * width)
      if heights[left] < heights[right]:
        left += 1
      else:
        right -= 1

    return max_area


if __name__ == '__main__':
  import doctest
  doctest.testmod()
