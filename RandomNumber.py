import random

secret = random.randint(1, 100)
attempts = 0

while True:
    
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
        
    if guess == secret:
        print(f"Correct {secret}")
        print(f"It took you {attempts} many tries.")
        break
    elif guess < secret:
        print("too low")
    elif guess > secret:
        print("too high")