# Magic-8Ball
I'm very new to coding and I use python 3. I wanted to make a automatic magic 8ball, after doing some research I found a version that seemed to work for the most part but I still had to put some information in. That is left bellow. My refined version is going to be in a file on its own. I think I'll also make one that will work by asking you if you'd like to reroll.

/ / / / / / / / / / / / / / / / / / / / / /
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
/ / / / / / / / / / / / / / / / / / / / / /

I didn't like how much spaghetti was in the code, using systems seemed really unreasonable but reading it from the right angle allowed me to see the bare bones of what this project actually needs.
If anyone can tell me why systems would be better than my own version, please let me know in a comment (i think you can do that right?)
