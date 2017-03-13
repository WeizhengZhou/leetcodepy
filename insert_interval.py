# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def insert(self, intervals, new_interval):
    merged = [new_interval, ]
    for i in range(len(intervals)):
      last = merged[-1]
      interval = intervals[i]
      if interval.end > last.start:
        merged[-1] = interval
        merged.append(last)


    return merged

if __name__ == '__main__':
  import doctest
  doctest.testmod()
