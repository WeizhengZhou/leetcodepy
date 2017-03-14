# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"

# Problem url.

from collections import deque


class Solution(object):
  """
  >>> solution = Solution()
  """

  def simplifyPath(self, path):
    stack = deque()
    d_list = path.split('/')

    for d in d_list:
      if not d:
        continue
      elif d == '..':
        if stack:
          stack.pop()
      elif d == '.':
        continue
      else:
        stack.append(d)

    return '/' + '/'.join(stack)



if __name__ == '__main__':
  s = Solution()
  print s.simplifyPath('/home/')
  print s.simplifyPath('/a/./../../c/')
