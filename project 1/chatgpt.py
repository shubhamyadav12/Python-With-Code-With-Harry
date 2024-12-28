'''
snake  1
water -1
gun  o
'''
import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choise (for snake type 's', for gun type 'g' and for water type 'w') : ")
youDict = {"s": 1, "w":-1, "g": 0}
you = youDict[youstr]
reverseDict = {1:"snake", -1:"water", 0:"gun"}
print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[you]}")

if   computer == you:
    print("its a draw")
else:
    if computer == 1 and you == -1:
       print("you are lose")      
    elif computer == -1 and you == 1:
        print("you are win")   
    elif computer == 0  and you == 1:
        print("you are win")   
    elif computer == 1 and you == 0:
        print("you are lose")   
    elif computer == -1 and you == 0:
        print("you are win")   
    elif computer == 0 and you == -1:
        print("you are lose")   

