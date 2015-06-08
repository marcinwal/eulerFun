#find the sum of all the digits in number 100!
import time

def factorial(number):
  fact = 1;
  for n in range(2,number+1):
    fact *= n 
  return fact

def sumDigits(number):
  n = number
  sum = 0
  while n > 0:
    sum += n % 10
    n /= 10
  return sum

def sumDigitsNice(number):
  return reduce(lambda x,y: x + ord(y) - ord('0'),list(str(number)),0)

time1 = time.time()
print sumDigits(factorial(1500))
run1 = time.time() - time1
time2 = time.time()
print sumDigitsNice(factorial(1500))
run2 = time.time() - time2

print(" time1 %s , time2 %s" %(run1,run2))