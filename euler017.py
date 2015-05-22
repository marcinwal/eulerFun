def solution(number):
  words ={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',
          9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourtheen',
          15:'fivteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',
          30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
          100:'hundred',1000:'thousand'}

  divisors = [1000,100]

  inner = number

  text = ''


  for divisor in divisors:
    result = inner / divisor

    if result > 1:
      inner %= divisor 
      text += words[result]+words[divisor]
    elif result == 1:
      inner %= divisor 
      text += words[1]+words[result*divisor]        

  if (inner < 20) and (inner >0):
      text += words[inner]
  elif inner > 0 :
      text += words[(inner/10)*10]
      if inner % 10 != 0:
        text += words[inner%10] 
      
  return text,len(text),number

def sum1to(number):
  sum = 0
  for i in range (1,number+1):
    result = solution(i)
    print result
    sum += result[1]

  return sum

def smart():
  n1_9 =  3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
  n10_19 = 3 + 6 + 6 + 8 + 8 + 7 + 7 +9 + 8 + 8
  n20_99 = 10*(6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8 * n1_9
  n100_1000 = n1_9 * 100 + 9 * (n1_9 + n10_19 + n20_99) + 7 * 9 + 9 * 99 * 10 

# print solution(11)
print sum1to(1000)
