def isPalindrome(myStr):

  myStr = myStr.lower()
  #reverse string python
  reversed = list(myStr)
  reversed.reverse()
  reversed = ''.join(reversed)
  #end reversed string

  if (myStr == reversed):
    return True
  else:
    return False

print(isPalindrome('Madamadam'))
