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

  if inner < 20:
      text += words[inner]
  else:
      text += words[(inner/10)*10]+words[inner%10]
      
  return text,len(text),inner

print solution(919)

