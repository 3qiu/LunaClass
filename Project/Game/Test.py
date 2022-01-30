import random


def matthew():
    points=0
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        #tries=int(input("How many tries would you like against the computer?"))
        user = input("Enter a choice (rock, paper, scissors): ")
        list = ["rock", "paper", "scissors"]
        computer = random.choice(list)
        print("You chose "+user+", the computer chose "+computer+".")
        

        if user == computer:
            print("Both players selected "+user+". It's a tie! You lose 0 points!")
        elif user == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win 2 points!")
                points=points+2
            else:
                print("Paper covers rock! You lose 1 point!")
                points=points-1
        elif user == "paper":
            if computer == "rock":
                print("Paper covers rock! You win 2 points!")
                points=points+2
            else:
                print("Scissors cuts paper! You lose 1 point!")
                points=points-1
        elif user == "scissors":
            if computer == "paper":
                print("Scissors cuts paper! You win 2 points!")
                points=points+2
            else:
                print("Rock smashes scissors! You lose 1 point!")
                points=points-1
        else:
            print("Listen to directions, you dingus!")



        print("Your score so far is "+str(points)+".")

        play_again = input("Would you like to play again? (y/n): ")
        if play_again != "y":
            break


    home=input("Would you like to return to the games list? (y/n): ")
    if home == "y":
        start()
        
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

def shemane():
    point=0
    while True: 
        print("Are you ready to roll a dice?")
        x=int(input("Roll the dice and enter a number from 1 to 6!"))
        print("you got "+str(x))

        y=random.randint(1,6)
        print("The computer got "+str(y))
        
        if x>y:
          point=point+1
          print("you win! and you got "+str(point)+" point!")
        
        else:
          print("player 1 win!")
              
        play_again=input("Would you like to play again? (y/n) ")
        if play_again != "y":
          break #has syntax error
    home=input("Would you like to return to the game selection? (y/n) ")
    if home == "y":
      start()  

def yanfei():
    print("Welcome to Tic Tac Toe, good luck!")
    point = 0
    
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

#  write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, user will declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        #  change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    home = input("Do want to play Again?(y/n)")
    if home == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

    if __name__ == "__main__":
        game()

    



def start():
  print("""                             -----Main Menu-----""")
  choice=input("""
                 
                 Please select what game you would like to play!
                 
                 A: Rock, Paper, Scissors - by Matthew Smith
                 B: Number Guesser - by Qiuyi
                 C: Are you ready to roll a dice - by Shemane Lewis
                 D: Tic Tac Toe - Yanfei Wu
                 E: Quit application
                
                 
                 """)
  if choice == "A" or choice == "a":
      matthew()
  elif choice == "B" or choice == "b":
      qiuyi()
  elif choice == "C" or choice == "c":
      shemane()
  elif choice == "D" or choice == "d":
      yanfei()
  elif choice == "E" or choice == "e":
        
      print("""
                If you'd like to play again, just re-run the application.
                Thanks for playing!
              """)

  else:
      print("Please input a valid command. ")
      start() 
start()
