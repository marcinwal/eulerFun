def answer():
  divisions = [11,12,13,14,15,16,17,18,19,20]
  number = 20
  while True:
    success = True
    for el in divisions:
      if number % el != 0:
        success = False
    if success:
      break
    else:
      number += 20
  return number

def generatePrimes(max):
  primes = []
  primes.append(2)  
  for i in range(3,max):
    isPrime = True
    j = 0

    while(primes[j] * primes[j] <= i):
      if( i % primes[j] == 0):
        isPrime = False
        break
      j += 1
         
    if isPrime:
      primes.append(i)
    i += 2

  return primes

#N = p1^a1*p2^a2 ... pi --> ith prime number
def smart(number):
  import math
  maxDivisor = number
  primes = generatePrimes(number)
  result = 1
  for prime in primes: 
    a = int(math.floor(math.log(maxDivisor)/math.log(prime)))
    # result = result * (math.pow(prime,a))
    result = result * (prime**a)
  return result


print answer()
# print generatePrimes(21)
print smart(20)