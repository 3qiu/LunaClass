import random
print("Are you ready to roll a dice?")
point=0
x=int(input("Roll the dice and enter a number from 1 to 6!"))
print("you got "+str(x))

y=random.randint(1,6)
print("player 1 got "+str(y))

if x>y:
    point=point+1
    print("you win! and you got "+str(point)+" point!")

else:
print("player 1 win!")