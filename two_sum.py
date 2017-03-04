class Solution(object): 
	def twoSum(self, nums, target):
	    index_by_num = {}
	    for i in range(len(nums)):
	    	index_by_num[nums[i]] = i

	    for i in range(len(nums)):
	    	rest = target - nums[i]
	    	rest_index = index_by_num.get(rest, None)
	    	if rest_index and rest_index != i:
	    		return (i, rest_index)




        