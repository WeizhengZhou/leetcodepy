# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):

  def lengthOfLongestSubstring(self, input_string):
    if not input_string:
      return 0 
    if len(input_string) <= 1:
      return len(input_string)
    seen_char_set = set()
    left = 0
    right = 1
    longest_length = 1

    seen_char_set.add(input_string[left])

    while right < len(input_string):
      while input_string[right] in seen_char_set:
        seen_char_set.remove(input_string[left])
        left += 1
      seen_char_set.add(input_string[right])
      longest_length = max(longest_length, right - left + 1)
      right += 1
    return longest_length


test_cases = ['abcabcbb', 'bbbbb', 'pwwkew']
solution = Solution()
for test_case in test_cases:
  print solution.lengthOfLongestSubstring(test_case)
