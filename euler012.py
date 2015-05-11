primes = []

def findPrimes(howManyPrimes):
  primes.append(2)
  n = 3 
  while len(primes) < howManyPrimes:
    j = 0
    isPrime = True
    while (primes[j] * primes[j] < n):
      if (n % primes[j] == 0):
        isPrime = False
        break
      j += 1
    if isPrime:
      primes.append(n)
    n += 1

def findPrimeDivisors(number):
  n = number
  divisors = []
  while n != 1:
    j = 0
    while (n % primes[j]!=0):
      j += 1
    if not (primes[j] in divisors):
      divisors.append(primes[j])
    n /= primes[j]
  return divisors  

def findAllDivisors(divisors,number):
  divisorsAll = divisors
  for i in range(0,len(divisors)):
    n = number
    while(n % divisors[i] == 0):
      n /=  divisors[i] 
      if not (n in divisorsAll):
        divisorsAll.append(n)
  return divisorsAll + [1] + [number]


def triangle(number):
  return number * (number + 1)/2

def countDivisiors(number):
  count = 0
  for i in range(1,number):
    if number % i == 0:
      count +=1
  return count

def find500slow():
  n = 4
  divisors = 0
  number = 1
  while divisors < 500:
    n += 1
    number = triangle(n)
    divisors = countDivisiors(number)
    print number,divisors
  return number

def solve(limit):
  findPrimes(500)
  n = 4
  allDivisors = []
  while len(allDivisors) < limit:
    n += 1
    number = triangle(n)
    divisors = findPrimeDivisors(number)
    allDivisors = findAllDivisors(divisors,number)
  return n,allDivisors,len(allDivisors)
    
findPrimes(500)
divisors = findPrimeDivisors(28)
print divisors
print findAllDivisors(divisors,28)
print solve(15)