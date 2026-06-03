import random

player_score=0
comp_score=0

choices=["r","p","s"]
while True:

    choice=input("Enter r/p/s: ").lower()

    if choice  not in choices:
        print("Enter r/p/s")
        continue

    comp_choice=random.choice(choices)

    print(f"Your Choice is {choice}")
    print(f"Comp Choice is {comp_choice}")

    if choice==comp_choice:
        print("It's a Tie !")
    elif (
        (choice=="r" and comp_choice=="s") or
        (choice=="p" and comp_choice=="r") or
        (choice=="s" and comp_choice=="p") 
        ):
            print("You Win !")
            player_score +=1
    else:
        print("Computer Wins !")
        comp_score +=1

    print(f"You {player_score}-{comp_score} Computer")
    print()
    
    if player_score >=3:
        ask=input("Play Again y/n: ").lower()
        if ask!="y":
            print("Bye (Fi-Amanillah ♥)")
            break