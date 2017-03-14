# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.


# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def plusOne(self, digits):
    n = len(digits)
    res = [0,] * (n + 1)
    carry = 1

    for i in range(n-1, -1, -1):
      carry += digits[i]
      res[i+1] = carry % 10
      carry /= 10

    res[0] = carry

    if res[0]:
      return res
    else:
      return res[1:]


if __name__ == '__main__':
  import doctest
  doctest.testmod()
