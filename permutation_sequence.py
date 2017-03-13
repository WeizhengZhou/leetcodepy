

class Solution(object):
  """
  >>> solution = Solution()
  """

  def getPermutation(self, n, k):
    if n <= 0:
      return ''
    if n == 1:
      return '1'

    facts = self.factorial(n)
    k -= 1

    used = [False,] * n
    res = [0,] * n
    for i in range(n-1):
      rank = k / facts[i+1]
      j = 0
      for j in range(n):
        if used[j]:
          continue
        else:
          rank -= 1
        if rank < 0:
          used[j] = True
          res[i] = (j + 1)
          break
      k = k % facts[i+1]

    i = n -1
    rank = 0
    j = 0
    for j in range(n):
      if not used[j]:
        res[i] = (j + 1)
        break
    return ''.join([str(r) for r in res])


  def factorial(self, n):
    if n <= 0:
      return []

    res = [1,] * n

    for i in range(1, len(res)):
      res[i] = res[i-1] * (i + 1)

    return res[::-1]  # Reversed.


if __name__ == '__main__':
  s = Solution()
  print s.getPermutation(3, 6)
  # import doctest
  # doctest.testmod()
