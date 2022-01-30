import random

def qiuyi():
  print("Hi there! Are you ready to test your instinct? Welcome to the Number Guessing Game")

  point=0
  count=0
  answer=0

  level=input("Select a level: Easy for 1 point, Intermediate for 5 points, Expert for 10 points.")
  while True:
    if level=="Easy":
        x=random.randint(1,10)
        while answer !=x:
            count=count+1
            answer=int(input("guess a number between 1 and 10:"))
            if answer<x:
                print("your number "+str(answer)+" is too low")
            elif answer>x:
                print("your number "+str(answer)+" is too high")
            else:
                point=point+1
                print("Yay! your answer "+str(answer)+" is correct")
                print("It took you "+str(count)+" tries and you got "+str(point)+" points!")

    elif level=="Intermediate":
        x=random.randint(1,30)
        while answer !=x:
            count=count+1
            answer=int(input("guess a number between 1 and 30:"))
            if answer<x:
                print("your number "+str(answer)+" is too low")
            elif answer>x:
                print("your number "+str(answer)+" is too high")
            else:
                point=point+5
                print("Yay! your answer "+str(answer)+"is correct")
                print("It took you "+str(count)+" tries and you got "+str(point)+" points!")

    elif level=="Expert":
        x=random.randint(1,50)
        while answer !=x:
            count=count+1
            answer=int(input("guess a number between 1 and 50:"))
            if answer<x:
                print("your number "+str(answer)+" is too low")
            elif answer>x:
                print("your number "+str(answer)+" is too high")
            else:
                point=point+10
                print("Yay! your answer "+str(answer)+" is correct")
                print("It took you "+str(count)+" tries and you got "+str(point)+" points!")

    else:
        level=input("Select a level: Easy for 1 point, Intermediate for 5 points, Expert for 10 points.")
        print("invalid response")
              
    play_again=input("Would you like to play again? (y/n) ")
    if play_again != "y":
      break
  home=input("Would you like to return to the game selection? (y/n) ")
  if home == "y":
    start()
