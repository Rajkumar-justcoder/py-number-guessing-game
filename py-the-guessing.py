from colorama import Fore


import random
import math

lower = int(input(Fore.BLUE + "Enter lower Range for Guessing:- "))


higher = int(input(Fore.BLUE + "Enter Higher Range for Guessing:- "))


x = random.randint(lower, higher)
print("\n\tYou've only ",
	round(math.log(higher - lower + 1, 2)), Fore.BLUE +
	" chances to guess the integer!\n")

count = 0


while count < math.log(higher - lower + 1, 2):
	count += 1
	guess = int(input(Fore.BLUE + " Guess a number:- "))

	# Condition testing
	if x == guess:
		print(Fore.BLUE + "Congratulations you did it in ",count, " try")
		break
	elif x > guess:
		print(Fore.BLUE + "You guessed too small!")
	elif x < guess:
		print(Fore.BLUE + "You Guessed too high!")
#made by Stack Coder https://github.com/Rajkumar-stackcoder/
if count >= math.log(higher - lower + 1, 2):
	print(Fore.BLUE + "\n The number is %d" % x)
