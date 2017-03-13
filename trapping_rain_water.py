# https://leetcode.com/problems/trapping-rain-water/?tab=Description


class Solution(object):
  """
  >>> solution = Solution()
  """

  def trap(self, heights):
    n = len(heights)
    
    left_bars = [0,] * n
    max_so_far = 0
    for i in range(0, n):
      left_bars[i] = max_so_far
      max_so_far = max(max_so_far, heights[i])
    
    right_bars = [0,] * n
    max_so_far = 0
    for i in range(n-1, -1, -1):
      right_bars[i] = max_so_far
      max_so_far = max(max_so_far, heights[i])

    area = 0

    for i in range(1, n-1):
      lower_bar = min(left_bars[i], right_bars[i])
      water_height = max(0, lower_bar - heights[i])
      area += water_height

    return area


if __name__ == '__main__':
  # heights = [0,1,0,2,1,0,1,3,2,1,2,1]
  heights = [5,2,1,2,1,5]
  s = Solution()
  print s.trap(heights)
  # import doctest
  # doctest.testmod()

