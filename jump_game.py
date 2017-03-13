# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def canJump(self, nums):
    if not nums:
      return True

    left, right = 0, 0

  def _nextRange(self, left, right, nums):
    if left > right:
      return None, None
    next_left, next_right = None, None
    curr = left

    while curr <= right:
      if not next_left:
        next_left = curr



if __name__ == '__main__':
  s = Solution()
  # print s.canJump([2,3,1,1,4])
  print s.canJump([3,2,1,0,4])
