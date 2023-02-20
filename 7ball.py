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
