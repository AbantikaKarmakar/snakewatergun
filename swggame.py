# Snake Water Gun
import random
n = 0
me = 0
comp = 0
print("You have 10 chances...")
while n < 10:
    print("1.Snake \n2.Water \n3.Gun")
    play = int(input("Enter your choice: "))
    lst = ["Snake", "Water", "Gun"]
    choice = random.choice(lst)
    print("Computer chose:", choice)
    if play == 1:
        if choice == "Water":
            me = me + 1
        elif choice == "Gun":
            comp = comp + 1
    elif play == 2:
        if choice == "Gun":
            me = me + 1
        elif choice == "Snake":
            comp = comp + 1
    elif play == 3:
        if choice == "Snake":
            me = me + 1
        elif choice == "Water":
            comp = comp + 1
    else:
        print("Invalid choice!!!")
        break
    n = n + 1
print("GAME OVER!!")
print("The scores are as follows:")
print("Computer =", comp, end=" ")
print("Your score =", me)
if comp > me:
    print("Computer Wins!! Better luck next time")
elif comp == me:
    print("The game is a tie")
else:
    print("You win!! Congratulations")