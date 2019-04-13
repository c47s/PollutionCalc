import os
from termcolor import colored
from termcolor import cprint
from textwrap import fill

rows, columns = os.popen('stty size', 'r').read().split()
os.system('color')
os.system('cls' if os.name == 'nt' else 'clear')
bottle = [
  " mmm ",
  " )-( ",
  "(   )",
  "|   |",
  "|___|",
]
maxRows = int((int(columns)) / 6) + 1
for row in bottle:
  for i in range(1, maxRows):
    print(colored(row, "blue"), end = " ")
  print("")
print("")
for col in range(1, int((int(columns) - 39) / 2)):
  print(" ", end = "")
cprint("P O L L U T I O N   C A L C U L A T O R", attrs = ["bold", "underline"])
print("")

trashItems = ["Plastic Bottles", "Plastic Cups", "Straws", "Cotton Swabs", "Cigarettes", "Plastic Bags", "pieces of Plastic Silverware", "Food Containers"]
score = 0
for trashItem in trashItems:
  notAnswered = 1
  while notAnswered == 1:
    print("\nHow many", colored(trashItem, "green"), "did you use today?")
    thing = input(colored("> ", attrs = ["dark"]))
    try:
      if trashItem == "Plastic Bottles":
        thing = int(thing) * 2
        notAnswered = 0
      else:
        thing = int(thing)
        notAnswered = 0
    except:
      print(colored("Please enter an integer", "red"))
  score += thing
try:
  inverseScore = round(100 / score, 1)
  inverseScore = str(inverseScore) + "%"
except ZeroDivisionError:
  inverseScore = "∞"
print(f"Your score is {colored(inverseScore, 'yellow')}.")
print("Higher is better.")
if score < 6:
  res = "are helping to protect the environment, because you create very little waste!"
elif score >= 6 and score < 18:
  res = "are doing good but you can always do better!"
else:
  res = "can do a lot more for the environment, it needs your help!"
print(f"Overall, you {res}")
print("")
print(colored(fill("""Toxic pollution affects more than 200 million people worldwide, according to Pure Earth, a non-profit environmental organization. In some of the world's worst polluted places, babies are born with birth defects, children have lost 30 to 40 IQ points, and life expectancy may be as low as 45 years because of cancers and other diseases."""), "red"))
print("\n")