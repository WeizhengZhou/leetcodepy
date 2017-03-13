# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Problem url.

class Solution(object):
  """
  >>> solution = Solution()
  """

  def merge(self, intervals):
    if not intervals or len(intervals) == 1:
      return intervals
    intervals.sort(key=lambda i: i.start)
    merged_intervals = [intervals[0],]
    for i in range(1, len(intervals)):
      if intervals[i].start > merged_intervals[-1].end:
        merged_intervals.append(intervals[i])
      else:
        merged_intervals[-1].end = max(intervals[i].end, merged_intervals[-1].end)
    return merged_intervals


if __name__ == '__main__':
  import doctest
  doctest.testmod()
