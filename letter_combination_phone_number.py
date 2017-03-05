# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?tab=Description

class Solution(object):
  """
  >>> Solution()._numToLetters(2)
  ['a', 'b', 'c']
  >>> Solution()._numToLetters(3)
  ['d', 'e', 'f']
  >>> Solution()._numToLetters(9)
  ['w', 'x', 'y', 'z']
  >>> Solution().letterCombinations('23')
  ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
  """

  NUMBER_TO_LETTER = {
      2: 'abc',
      3: 'def',
      4: 'ghi',
      5: 'jkl',
      6: 'mno',
      7: 'pqrs',
      8: 'tuv',
      9: 'wxyz'
  }

  def letterCombinations(self, digit_strs):
    if not digit_strs:
      return []
    curr_letters = self._numToLetters(int(digit_strs[0]))
    if len(digit_strs) == 1:
      return curr_letters
    rest_combinations = self.letterCombinations(digit_strs[1:])
    all_combinations = []
    for curr_letter in curr_letters:
      for rest_combination in rest_combinations:
        all_combinations.append(curr_letter + rest_combination)
    return all_combinations

  def _numToLetters(self, x):
    assert 2 <= x <= 9, '%d not in range [2, 9]' % x
    return [l for l in self.NUMBER_TO_LETTER[x]]
    


if __name__ == '__main__':
  print Solution().letterCombinations('23')
  # import doctest
  # doctest.testmod()
