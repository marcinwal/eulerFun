
#a<b<c
#so a < s/3 , a<b<s/2
def triplet():
  a,b,c = 0,0,0
  s = 1000
  found = False
  for a in range(1,s/3):
    for b in range(a,s/2):
      c = s - a - b
      if (a * a + b * b == c * c):
        found = True 
        break
    if (found):
      break
  return (a,b,c,a*b*c)


print triplet()