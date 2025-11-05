import random

a = random.randint(1,100) 
max_attempt = 10
attempt = 0

while attempt < max_attempt   :
    try :
        guess = int(input("Guess the number = "))
        attempt += 1
        if guess < a:
            print("Its Low")
        elif guess > a:
            print("Too High")
        else:
            print(f"You GOT the Number!! in {attempt} attempt")
            break
    except ValueError:
        print("Enter a valid number")
else:
    print(f"OUT OF ATTEMPTS the number was {a}")

    
