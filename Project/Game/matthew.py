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
        



        
def start():
    print("-----Main Menu-----")
    choice=input("""
                 
                 Please select what game you would like to play!
                 
                 A: Rock, Paper, Scissors - by Matthew Smith
                 B: Number Guesser - by Quiyi
                 C: Hangman - by Shemane
                 D: Tic Tac Toe - Yanfei Wu
                 E: Display your total score.
                 F: Quit application
                
                 
                 """)
    if choice == "A" or choice == "a":
        matthew()
    elif choice == "B" or choice == "b":
        qiuyi()
    elif choice == "C" or choice == "c":
        quiyi()
    elif choice == "D" or choice == "d":
        quiyi()
    elif choice == "E" or choice == "e":
        total=total + points
        print("Your total score is "+points+".")
    elif choice == "F" or choice == "f":
        print("""
                If you'd like to play again, just re-run the application.
                Thanks for playing!
              """)
    else:
        print("Please input a valid command. ")
        start() 
start()