def answer(number):
  sum = 0 
  for i in range(1,number):
    for j in range(i+1,number+1):
      sum += 2*i*j
      print i,j
  return sum


print answer(100)