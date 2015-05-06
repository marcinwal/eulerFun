import timeit

def fibonaci(number):
  sum = 0
  prev = 1
  curr = 1
  result = 0
  while True:
    if curr > number:
      break
    result = prev + curr  
    prev = curr
    curr = result
    if curr % 2 == 0:
      sum += curr
  return sum

def better(number):
  fib3 = 2
  fib6 = 0 
  result = 2
  sum = 0
  while(result < 4000000):
    sum += result

    result = 4 * fib3 + fib6 
    fib6 = fib3 
    fib3 = result
  return sum

print fibonaci(4000000)
print better(4000000)
print(timeit.timeit("fibonaci(4000000)",setup="from __main__ import fibonaci"))
print(timeit.timeit("better(4000000)",setup="from __main__ import better"))