def answer(number):
  sum = 0 
  for i in range(1,number):
    for j in range(i+1,number+1):
      sum += 2*i*j
  return sum

def analytical(number):
  sum = number *(number + 1) / 2
  squared = (number * (number + 1) * (2 * number + 1)) / 6
  return sum * sum - squared

print answer(100)
print analytical(100)