def isPalindrom(string):
  if len(string) <= 1:
    return True
  if (string[0] != string[-1]):
    return False
  return isPalindrom(string[1:-1])
  
def findMaxThreeDigitsMultPalindrom():
  max=(0,0,0)
  for i in range(100,999):
    for j in range(i,999):
      number = i * j
      if isPalindrom(str(number)) and number>max[0]:
        max = (number,i,j)
  return max      


print findMaxThreeDigitsMultPalindrom()  
