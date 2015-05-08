def primes(which):
  primes = []
  primes.append(2)
  i = 3
  while len(primes) < which:
    j = 0
    isPrime = True
    while(primes[j]*primes[j] <= i):
      if(i % primes[j] == 0):
        isPrime = False
        break
      j += 1  
    if isPrime:
      primes.append(i)
    i += 2
  return primes[-1]  

print primes(10001)