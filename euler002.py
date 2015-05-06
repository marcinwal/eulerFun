def fibonaci(number):
  result = 0
  prev = 1
  curr = 1
  sum = 0
  while (result < number):
    if((result % 2) == 0):
      sum += result
    result = prev + curr
    prev = curr
    curr = result 
  return sum

print fibonaci(4000000)