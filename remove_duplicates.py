# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?tab=Description

class Solution(object):
  """
  >>> s = Solution()
  >>> s.removeDuplicates([1,])
  1
  >>> s.removeDuplicates([1, 1, 2])
  2
  >>> s.removeDuplicates([1, 3, 3, 3, 5, 6, 6])
  4
  """

  def removeDuplicates(self, nums):
    if not nums:
      return 0
    if len(nums) == 1:
      return 1
    tail = 0
    curr = 1
    while curr < len(nums):
      if nums[curr] != nums[tail]:  # Compare with tail of sorted list.
        tail += 1
        nums[tail] = nums[curr]
      curr += 1
    return tail + 1


if __name__ == '__main__':
  import doctest
  doctest.testmod()
