#This program is based off the trivia show Bullsh*t! on Netflix, I thought it would be interesting to try and replicate the game in Python, so here are the rules of the game
# Rule 1 The hotseatuser must answer the question Between (A,B,C,D) then explain their answer 
# Rule 2 Three other users must decide if the answer is true or not, if all three users choose not to believe the hotseatuser, and the answer they provided is wrong the game ends, and a new trivia session begins.
# Right now it will probably use the same questions over and over but I want it to eventually by alot of questions in a random order.
# I'm thinking through this by myself at the moment and I'll comment out my process to explain the code.

#Step one, No code for this one I am going to find a list of 25 trivia questions online and create a txt file.
# Done txt file called trivia.txt questions pulled from https://www.quiztriviagames.com/multiple-choice-trivia-questions/

#Now the first thing I did was to test the file and see if I could only print the questions I will comment out this code but I left it for you guys incase you wanted to follow along.

#def openingthetrivia():
    #fBSQNA = open('trivia.txt')
#I know its cool to have an input but as of 02/17 I only have the one trivia file so no need, edit as you please though!
    #for line in fBSQNA:
        #if line.startswith('.'):
           #print(line)
        #else:
            #continue

#openingthetrivia()
#Ok so the code above was above was a success, i do wonder if I can make it starts with numbers inseat of '.'?
#You know what I'm going to try below
fBSQNA = open('trivia.txt')

def openingthetrivia():
    for line in fBSQNA:
        if line.startswith('.'):
            print(line)
        else:
            continue

#openingthetrivia()

#Tried to convert every int to a string using ints = str(int) if line startswith(ints): print(line) but did not work, can you help me out what do you think.
# Whatever it was a nice thought for QOL but I can continue, next I am going to print the just the answers.

def openingtheanswers():
    for line in fBSQNA:
        if line.startswith("A"):
            print(line)
        elif line.startswith("B"):
            print(line)
        elif line.startswith("C"):
            print(line)
        elif line.startswith("D"):
            print(line)
        else:
            continue

#openingtheanswers()
#Ok cool got the answers now I need to try to add these together to get a single question and a single set of answers.

def openingQNA():
    for line in fBSQNA:
        Question = line.startswith('.')
        AnswerA = line.startswith('A')
        AnswerB = line.startswith('B')
        AnswerC = line.startswith('C')
        AnswerD = line.startswith('D')
        if Question is True:
            print(line)
        elif AnswerA is True:
            print(line)
        elif AnswerB is True:
            print(line)
        elif AnswerC is True:
            print(line)
        elif AnswerD is True:
            print(line)
        else:
            continue

openingQNA()
#Ok we have something here and  I know its the long way aroud from for line in blah: print(line) but i'm just thinking through it right now, no reason to judge.....

