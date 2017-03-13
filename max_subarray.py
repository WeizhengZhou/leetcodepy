# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def maxSubArray(self, nums):
    if not nums:
      return 0 
    if len(nums) == 1:
      return nums[0]

    curr_sum = nums[0]
    max_sum = curr_sum
    i = 1
    while i < len(nums):
      if curr_sum <= 0:
        curr_sum = nums[i]
      else:
        curr_sum += nums[i]
      max_sum = max(curr_sum, max_sum)
      i += 1

    return max_sum


if __name__ == '__main__':
  s = Solution()
  print s.maxSubArray([-2, -1])
  # print s.maxSubArray([1,2,3])
  # print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])