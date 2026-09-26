'''
This is a simple Python program.
1  for snake game
-1 for water
0 for gun
'''
import random

computer_choice = random.choice([1, -1, 0] )
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

youDict = {'s':1, 'w':-1, 'g':0}
you = youDict[youstr]

reverse_youDict = {1:'snake', -1:'water', 0:'gun'}
reverse_computerDict = {1:'snake', -1:'water', 0:'gun'}

print(f"Computer chose: {reverse_computerDict[computer_choice]}")
print(f"You chose: {reverse_youDict[you]}")

if computer_choice == you:
    print("It's a tie!")
elif (computer_choice == 1 and you == -1) or (computer_choice == -1 and you == 0) or (computer_choice == 0 and you == 1):
    print("Computer wins!")

elif (computer_choice == -1 and you == 1) or (computer_choice == 0 and you == -1) or (computer_choice == 1 and you == 0):
    print("You win!")

else:
    print("Invalid input. Please enter 's' for snake, 'w' for water, or 'g' for gun.")            
