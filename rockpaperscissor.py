import random

userinput = 0
computerinput = 0
ties = 0

while True:
    a = random.randint(1,3)
    enter = input("Rock , Paper, Scissor = ").lower()

    if enter == "q":
            print("Game Over. Thanks for playing!")
            break

    if enter == "rock":
            user = 1
    elif enter == "paper":
            user = 2
    elif enter == "scissor":
            user = 3
    else:
         print("Invalid input. Try again.")
         continue
            

    match a:
        case  1 :
                print("ROCK")
        case 2:
            print("PAPER")
        case 3:
            print("SCISSOR")

    if a == user:
            print("Tie!")
            ties+=1
    elif (user == 1 and a == 3) or (user == 2 and a == 1) or (user == 3 and a == 2):
          print("You Win!")
          userinput+=1
    else:
            print("LOST")
            computerinput+=1
    print(f"Score: You {userinput} - Computer {computerinput} - Ties {ties}\n")
            