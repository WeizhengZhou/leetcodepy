# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def addBinary(self, a, b):
    m = len(a)
    n = len(b)
    i = m -1
    j = n -1
    carry = 0
    res = [0,] * (max(m, n) + 1)
    k = max(m, n)
    while i >= 0 or j >= 0:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1

      res[k] = carry % 2
      carry /= 2
      k -= 1
    res[0] = carry
    res = ''.join([str(r) for r in res])
    if res[0] == '0':
      return res[1:]
    else:
      return res


if __name__ == '__main__':
  s = Solution()
  print s.addBinary('11', '10')
