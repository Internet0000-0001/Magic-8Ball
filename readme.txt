let it first be known that I'm a very new coder and I will speak in simple terms, not to mention over analyse things that may be simple to others.
So the code that i found was this:
################
import sys
import random

ans = True

def Question_Fetch(Response):
  answers = random.randint(1,8)
  QuestionSet = ["It is certain","Outlook good","You may rely on it","Ask again later","Concentrate and ask again","Reply hazy, try again","My reply is no","My sources say no"]
  if Response == "":
    sys.exit()
  else:
    return str(QuestionSet[answers-1]);
while ans:
  question = input("Ask the magic 8 ball a question:  ")
  print(Question_Fetch(question))
###################

What I didn't like about this was the fact that it was so long, used functions like systems and asked you to write something for it to actually work, I just wanted it to 
tell me the answer. 

Line 10,11 and 15 were useful to inspire me to see what the bare bones of this code was, which at the end is all we need in any code.
I think that my method is smaller, cleaner and requires less functions. If anyone can give me a reason as to why we would you systems over simple code, let me know.
