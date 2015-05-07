

def findPrimeDivisorMax(number):
  largest = 0;
  for i in range(2,number):
    if (number % i == 0):
      isPrime = True
      for j in range(2,i):
        if(i % j == 0):
          isPrime = False
          break
      if (isPrime):
        largest = i;
  return largest

# any int can be decomposed into primes multiplications or is a prime number!
def findPrimeDivisorMaxBest(number):
  largest = 0
  counter = 2
  numb = number
  while (counter * counter <= numb):
    if(numb % counter == 0):
      numb = numb/counter
      largest = counter
    else:
      counter += 1
  if (numb > largest):
    largest = numb
  return largest

print findPrimeDivisorMaxBest(600851475143)
print findPrimeDivisorMax(1111)
print findPrimeDivisorMaxBest(1111)