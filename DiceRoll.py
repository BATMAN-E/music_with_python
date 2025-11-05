import random

while True:
    choice = input('Enter Your Coice:(Y/N)- ').lower()
 
    if choice == 'y':
        die1= random.randint(1, 6)
        die2= random.randint(1, 6)
        print(f'({die1},{die2})')
    elif choice == 'n':
        print('Thanks for Playing')
        break
    else:
        print("Invalid Choice")
