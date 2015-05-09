

def primesSum(maxNumber):
  primes = []
  primes.append(2)
  i = 3
  while primes[-1] < maxNumber:
    j = 0
    isPrime = True
    while(primes[j]*primes[j] <= i):
      if(i % primes[j] == 0):
        isPrime = False
        break
      j += 1  
    if isPrime:
      primes.append(i)
      print i 
    i += 2
  return reduce(lambda x,y: x+y,primes)-primes[-1]

print primesSum(2000000)