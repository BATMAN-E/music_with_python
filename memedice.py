import random

rolled = False  

while True:
    choice = input("Wanna roll the dice? (Y/N): ").lower()

    if choice == 'y' and not rolled:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2}) 🎲")
        rolled = True
    elif choice == 'y' and rolled:
        print("Bro stop 💀 find a GF to play with 😭")
        break
    elif choice == 'n':
        print("Smart choice. Go touch some grass 🌱")
        break
    else:
        print("Invalid input. It’s literally Y or N 😑")
