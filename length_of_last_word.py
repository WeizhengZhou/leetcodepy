

def lengthOfLastWord(self, s):
  if not s:
    return ''
  return s.split(' ')[-1]