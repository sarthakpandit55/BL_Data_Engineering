import random

jackpot = random.randint(1,100)
guess = int(input("Guess a number between 1 to 100: "))
attempts = 1

while guess != jackpot:
    if guess < jackpot:
        print("higher number")
    else:
        print("lower number")

    guess = int(input("Guess a number between 1 to 100: "))
    attempts += 1

print("You are correct")
print(f"You took {attempts} attempts")