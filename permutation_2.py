# Problem url.




class Solution(object):
  """
  >>> solution = Solution()
  """

  def permuteUnique(self, nums):
    if not nums:
      return [[],]
    if len(nums) == 1:
      return [[nums[0],],]
    
    counter = dict()

    for num in nums:
      if not counter.get(num):
        counter[num] = 1
      else:
        counter[num] += 1

    solution = [None] * len(nums)
    solutions = []
    self._buildSolutions(solution, 0, counter, solutions)
    return solutions


  def _buildSolutions(self, solution, index, counter, solutions):
    if index >= len(solution):
      return solutions.append(solution[:])

    for key in counter.keys():
      if counter[key] > 0:
        solution[index] = key
        counter[key] -= 1
        self._buildSolutions(solution, index + 1, counter, solutions)
        counter[key] += 1



if __name__ == '__main__':
  s = Solution()
  # print s.permuteUnique([1, 1, 2])
  print s.permuteUnique([2,2,2,3])

