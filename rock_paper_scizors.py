import random
choices = ["rock", "paper", "scizors"]

while True :
    com_choice = random.choice(choices)
    player_chioce = input("Rock paper scizors or (q) to quit ???... ")
    if player_chioce.lower() == "q":
        quit()
    if not player_chioce.lower() in choices:
        print("stubid !")
        quit()

    print(com_choice)
    if com_choice == player_chioce.lower() :
        print("try again")
    #elif player_chioce.lower() == "rock" and com_choice == "papar":
     #   print("computer wins")
    elif player_chioce.lower() == "rock" and com_choice == "scizors":
        print("congratiolation you win")
        quit()
    elif player_chioce.lower() == "paper" and com_choice == "rock" :
        print("congratiolation you win")
        quit()
   # elif player_chioce.lower() == "paper" and com_choice == "scizors" :
   #     print("computer wins")
   # elif player_chioce.lower() == "scizors" and com_choice == "rock" :
    #    print("computer wins")
    elif player_chioce.lower() == "scizors" and com_choice == "paper" :
        print("congratiolation you win")
        quit()
    else:
        print("computer wins")
