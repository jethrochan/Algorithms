def reverse(string):
    string = string[::-1]
    return string

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
