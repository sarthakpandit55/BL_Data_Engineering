import random

stake = int(input("Enter initial stack :- "))
goal = int(input("Enter the goal :- "))

wins = 0
bets = 0

while stake > 0 and stake < goal:
    user_stake = input("Choose Heads or Tails : ").lower()
    if user_stake not in ["heads", "tails"]:
        print("You have to choose Heads or Tails")
        continue

    flip = random.choice(["heads", "tails"])
    bets += 1

    if user_stake == flip:
        stake += 1
        wins += 1
        print("You win $1")
    else:
        stake -= 1
        print("You lose $1")

    print(f"Current stake: {stake}")
print("=" * 40)

if stake == goal:
    print("You reached your goal")
else:
    print("You are broke")

print("-" * 40)
print(f"Total Bets: {bets}")
print(f"Total Wins: {wins}")
print(f"Win percentage: {wins/bets*100}%")
print(f"Loss percentage: {wins/bets*100}%")