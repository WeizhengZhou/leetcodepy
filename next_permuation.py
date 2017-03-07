# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.nextPermutation([1,2,3])
  """

  def _swap(self, nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

  def nextPermutation(self, nums):
    if not nums or len(nums) <= 1:
      return
    if len(nums) == 2:
      self._swap(nums, 0, 1)
      return 
    
    index_to_swap = len(nums) - 2
    # Find the index to swap. 
    # It should be the first non-ascending index, viewing from right.
    while index_to_swap >= 0 and nums[index_to_swap] >= nums[index_to_swap + 1]:
      index_to_swap -= 1
    # Now nums[index_to_swap] < nums[index_to_swap-1],
    # and it's all sorted on the right of index_to_swap (include).

    # Find the smallest value on the right, that larger than nums[index_to_swap]
    value = nums[index_to_swap]

    min_value_index = index_to_swap + 1
    for i in range(index_to_swap + 1, len(nums)):
      if nums[i] > value and nums[min_value_index] > nums[i]:
        min_value_index = i

    self._swap(nums, index_to_swap, min_value_index)

    nums[index_to_swap + 1:] = sorted(nums[index_to_swap + 1:])



if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
  solution = Solution()
  nums = [1,3,2]
  solution.nextPermutation(nums)
  print nums
