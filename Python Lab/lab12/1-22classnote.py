import time
start=time.time()
for i in range(100)
print("hello")
end=time.time()
print(end-start)



import random

x = random.randint(1,10)
n=0
for x in range(1, 10):
    guess = int(input("What is your guess?"))
    print("the system has "+str(x), "you enter "+str(guess))
    n=n+1 # every attempt +1
    if x<guess:
        print("Too High")
        
    elif x>guess:
        print("Too low")
    else:
        print("Right!")
        
    if x==guess:
        print ("you took "+str(attempts)+" times to get it right")
        print("the total attemps number", n)
        
       
       
import time 

start = time.time()
for i in range(10):
    print("Right!")


import random
number = random.randint(1, 10)
attempts = 0  # count no of attempts to guess the number
guess = 0
while guess != number:
    guess = int(input("Guess a number: "))
    attempts += 1
    if guess == number:
        print ("Correct! You used", attempts, "attempts!")
        break
    elif guess < number:
        print ("Too Low!")
    else:
        print ("Too High!")
end = time.time()
print(end-start)
        
     

import random
number = number = random.randint(1, 10)
attempt=int(input("how many time you want to play?"))

point=0 #initial point
for x in range(attempt):
    guess=int(input("Guess a number:"))
    print ("Your number is "+str(guess), "The system has "+str(number))
    
    if x==guess:
        print ("you are correct")
        apoint= +10 #actual point
    else:
        print("you are wrong")
        apoint= -10 #actual point

    tpoint=point+apoint
    print("your total point is "+str(tpoint))
    
    
#manpal
import time
import random
start=time.time()
attempts=0
x=random.randint(1,10)
guess=int(input("guessing number from 1-10"))

if guess!=x:
    while guess!=x:
        print("your number is ",guess)
        print("the system has",x)
        if guess>x:
            print("Too high")
        else:
            print("Too low")
        
        guess=int(input("guessing number from 1-10"))
else:
    print("Correct")
attempts=attempts+1

print ("number of attempts is", attempts)

end=time.time()
print(end-start)

#rocky
import random
import time
start=time.time()

count=0
answer=0

level=input("what level player are you? beg, med or adv?")

if level=="beg":
    x=random.randint(1,10)
    while answer !=x:
        count=count+1
        answer=int(input("guess a number bw 1 and 10:"))
        if answer<x:
            print("your number"+str(answer)+"is too low")
        elif answer>x:
            print(str(answer)+" too high")
        else:
            print("your answer"+str(answer)+" is correct")
            print("it tooks "+str(count)+" tries")

elif level=="med":
    x=random.randint(1,50)
    while answer !=x:
        count=count+1
        answer=int(input("guess a number bw 1 and 50:"))
        if answer<x:
            print("your number"+str(answer)+"is too low")
        elif answer>x:
            print(str(answer)+" too high")
        else:
            print("your answer"+str(answer)+" is correct")
            print("it tooks "+str(count)+" tries")

elif level=="adv":
    x=random.randint(1,100)
    while answer !=x:
        count=count+1
        answer=int(input("guess a number bw 1 and 100:"))
        if answer<x:
            print("your number"+str(answer)+"is too low")
        elif answer>x:
            print(str(answer)+" too high")
        else:
            print("your answer"+str(answer)+" is correct")
            print("it tooks "+str(count)+" tries")

else:
    level=input("what level player are you? beg, med or adv?")
    print("invalid response")
            
end=time.time()
print(end-start)
        

        
#matt
import time
import random
start=time.time()

x=random.randint(1,10)
print("the system shows",x)
attemps=0
points=0
total=0

b=int(input("how many round would you like to play"))
for attempts in range(b):
    

guess=int(input("guessing number from 1-10"))




roll=int(input("how many rolls do you want to play"))
print ("rolls:",roll)


#question:
import random
number = random.randint(1, 10)
attempt=int(input("how many time you want to play?"))

point=0 #initial point
for x in range(attempt):
    guess=int(input("Guess a number:")) #syntax error?
    print ("Your number is "+str(guess), "The system has "+str(number))
    
    if x==guess:
        print ("you are correct")
        apoint= +10 #actual point
    else:
        print("you are wrong")
        apoint= -10 #actual point

    tpoint=point+apoint
    print("your total point is "+str(tpoint))
    '''

#question: the random have sequence number 
import random


n=0
for a in range(1, 10):
    x = random.randint(1,10)
    guess = int(input("What is your guess?")) 
    print("the system has "+str(x), "you enter "+str(guess))
    n=n+1 # every attempt +1
    while a!=x:
        if x<guess:
            print("Too High")

        elif x>guess:
            print("Too low")
            
print ("you took "+str(n)+" times to get it right")

        
'''
count=0
while count<5:
    print("the count is:",count)
    count=count+1
print("good bye")
        

bikes=["trek","cannodale","redline"]
print(bikes)

bikes=["trek","cannodale","redline"]
print(bikes[2])


bikes=["trek","cannodale","redline","buio","dryb"]
print(bikes[0:3])
        #index 0 is inclusice and 3 is exclusive
        
bikes=["trek","cannodale","redline","buio","dryb"]
print(bikes[1:2])        
        
bikes=["trek","cannodale","redline","buio","dryb"]
item
print("i want to buy",bikes[1:2]) 



numbers=[1,4,3,6,2]
print("before:")
print(numbers)
print("length:{}".format(len(numbers)))


numbers.append(99)
print("after:")
print(numbers)
print("length:{}".format(len(numbers)))

numbers.insert(2,99)
print("after:",numbers)


numbers.remove(2)
print("after:", numbers) 




x=abs(-5)//turns the absolute value of 5
print(x)//


def my_first_func():
    print("testing...")
    print("it works")
my_first_func()
      
 
def happy:
    print("testing...")
    print("it works")
my_first_func()        
        




