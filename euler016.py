def powerDigitsSum(power):
  result = 2**power
  resultList = list(str(result))
  sum = 0
  for el in resultList:
    sum += ord(el) - ord('0')

  print sum

powerDigitsSum(1000)