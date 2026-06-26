import random
rock=("""
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
""")

# Paper
paper=("""
     ___
---'    _)_
           __)
          ___)
         ___)
---.____)
""")

# Scissors
scissors=("""
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
""")
game_setup=[rock,paper,scissors]
user_choice=int(input("enter your choice  0 for 'rock',"
                      " 1 for 'paper', 2 for "
                      "'scissors':\n"))
print(game_setup[user_choice])
computer_choice=random.randint(0,2 )
print(f"computer choice is ")
print(game_setup[computer_choice])
if user_choice>=3 or user_choice<0:
    print("invalid number")
elif user_choice>=3 or user_choice<0:
    print("invalid number")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif user_choice<computer_choice:
    print("you lose")
elif computer_choice==user_choice:
    print("draw")
elif user_choice>computer_choice:
    print("you win ")