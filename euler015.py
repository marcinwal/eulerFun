def grid(number):
  numberOfBits = 2 * number
  sum = 0
  for i in range (1,2**(numberOfBits)):
    candidate = bin(i)
    extraZeros = 2 + numberOfBits - len(candidate)
    howManyZeros = len(candidate.split('0'))- 2 + extraZeros
    howManyOnes = len(candidate.split('1')) - 1
    if ((howManyZeros == number) and (howManyOnes == number)) :
      sum += 1
  return sum


# 2N
#  N 
# i choose N elements out of 2N where order does not matter
# (n over k ) = (n-k)!/k!

def smartGrid(number):
  paths = 1
  for i in range(0,number):
    paths = paths * (2* number - i)
    paths /= i + 1 
  return paths

# print grid(10)
print smartGrid(20)