# Problem url.


from collections import Counter
class Solution(object):
  """
  >>> solution = Solution()
  >>> solution.findSubstring('barfoothefoobarman', ['foo', 'bar'])
  [0, 9]
  >>> s = 'lingmindraboofooowingdingbarrwingmonkeypoundcake'
  >>> words = ["fooo","barr","wing","ding","wing"]
  >>> solution.findSubstring(s, words) 
  [13]
  """

  def findSubstring(self, s, words):
    if not words:
      return []
    if not words[0]:
      return []
    
    word_count = len(words)
    word_length = len(words[0])
    substr_length = word_count * word_length
    
    if len(s) < substr_length:
      return []
    
    counter = Counter(words)
    solutions = []
    for i in range(0, len(s)):
      sub_str_words = [
          s[j : j + word_length]
          for j in range(i, i + substr_length, word_length)
      ]
      curr_counter = Counter(sub_str_words)
      if curr_counter == counter:
        solutions.append(i)
    return solutions
    

if __name__ == '__main__':
  import doctest
  doctest.testmod()
