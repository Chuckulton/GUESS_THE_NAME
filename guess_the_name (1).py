import time 
import random

answerNum = 0
answer = ""
tries = 3
points = 0
streak = 0

print("TRIES",tries)
print("POINTS",points)

print("HUGH, JAMES, OSKAR, RYLAN")

while tries > 0:
    answerNum = (random.randint(1,4))
    
    if answerNum == 1:
        answer = "HUGH"
        
    if answerNum == 2:
        answer = "JAMES"
    
    if answerNum == 3:
        answer = "OSKAR"
        
    if answerNum == 4:
        answer = "RYLAN"
    
    print()
    
    guess = input("INPUT GUESS HERE >>")
    
    if guess == answer:
        print()
        
        print("CORRECT!")
        streak +=1
        tries += 1*streak
        points +=1*streak
        
        print("STREAK",streak)
        print("TRIES",tries)
        print("POINTS",points)
        
        
    else:
        print()
        print("INCORRECT!")
        tries -= 1
        print("TRIES",tries)
        print("POINTS",points)

        
        
        

