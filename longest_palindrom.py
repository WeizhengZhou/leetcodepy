class Solution(object):
  """
  >>> Solution().longestPalindrome('ab')
  'a'
  >>> Solution().longestPalindrome('aba')
  'aba'
  """

  def longestPalindrome(self, s):

    if not s:
      return 0
    n = len(s)
    if n == 1:
      return s[0]
    matrix = [[False for j in range(n)] for i in range(n)]

    for i in range(n):
      matrix[i][i] = True
    
    longest_length = 1
    longest_substr = s[0]
    for k in range(1, n):
      for i in range(0, n - k):
        j = i + k
        if i+1 >= j-1:
          matrix[i][j] = s[i] == s[j] 
        else:
          matrix[i][j] = matrix[i+1][j-1] and (s[i] == s[j])  
        if matrix[i][j]:
          longest_length = max(longest_length, j - i + 1)
          longest_substr = s[i:j+1]
    return longest_substr   


if __name__ == "__main__":
  import doctest
  doctest.testmod()
