import random

y = True
ans = random.randrange(1,20)
qus = ('It is certain. ','It is decidedly so. ', 'Without a doubt. ','Yes definitely. ','You may rely on it. ','As I see it, yes. ','Most likely. ','Outlook good. ','Yes. ','Signs point to yes. ','Reply hazy, try again. ','Ask again later. ','Better not tell you now. ','Cannot predict now. ','Concentrate and ask again. ',"Don't count on it. ",'My reply is no. ' ,'My sources say no. ', 'Outlook not so good. ', 'Very doubtful.')

while y == True:
    print(str(qus[ans-1]))
    break
