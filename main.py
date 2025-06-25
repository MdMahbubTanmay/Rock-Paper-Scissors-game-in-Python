import random

item=["Rock","Paper","Scissors"]

print("Computer Is Thinking...\nComputer Choosed Something\nNow Your Turn.Enter 1 , 2 or 3\n1 for Rock\n2 for Paper\n3 for Scissors")




def inputTaker():
 global inp
 inp = int(input("Enter: "))

inputTaker()


while inp not in [1,2,3]:
    print("Enter 1 , 2 or 3")
    inputTaker()
else:
   print("Calculating...")



computerChoice = random.choice(item)
playerChoice = item[inp-1]

if playerChoice == computerChoice:
   result = "Tie"
   
elif (playerChoice == "Rock" and computerChoice == "Scissors") or (playerChoice == "Paper" and computerChoice == "Rock") or (playerChoice == "Scissors" and computerChoice == "Paper"):
  result = "You Win"


else:
  result = "Computer Win" 



print(f"You Choose: {playerChoice}")
print(f"Computer Choose: {computerChoice}")
print(f"Result: {result}")
