def chain(number):  
  if number == 1:
    return 1  
  if number % 2 == 0:
    return 1+chain(number/2)
  else:
    return 1+chain(3*number+1)

def bruteForce():
  max = 9
  number = 13
  for i in range(14,1000000):
    res = chain(i)
    if (res > max):
      max = res
      number = i

  return(max,number)

def withCache(number):
  cache = {}
  cache[1] = 1
  sequenceLength = 0
  sequenceNumber = 0

  for i in range(2,number):
    sequence = i
    k = 0
    while ((sequence != 1) and (sequence >= i)):
      k += 1
      print sequence
      if (sequence % 2 == 0):
        sequence = sequence / 2 
      else:
        sequence = sequence * 3 + 1

    cache[i] = k + cache[sequence]

    if (cache[i] > sequenceLength): 
      sequenceLength = cache[i]
      number = i

  return sequenceNumber,sequenceLength,cache

# arr = []
# print chain(999)
# print bruteForce()
print withCache(999999)