import random
USER_NUM = 0
PLAYER_NUM = 0
select = ['rock', 'scissor' , 'paper']

while True:
    user_select = input("please Enter your choies between ROCK...SCISSOR...PAPPER=>")
    if   user_select == 'a':
        break



    if user_select not in select:
        print("Ooooops try agian")
        continue


        random_select = random.randint(0,2)
        player=select( random_select)
        print(f"Choies of player ==> {player}")


        if user_select == player:
            print(f"Equal print agian...")

        elif user_select == "rock" and player == "sicssor":
            print(f"Good job you win =) | +1 Number")
            USER_NUM += 1

        elif user_select == "paper" and player == "rock":
            print(f"Good job you win =) | +1 Number")
            USER_NUM += 1

        elif user_select == "sicssor" and player == "paper":
            print(f"Good job you win =) | +1 Number")
            USER_NUM += 1

        else:
            print("Sorry! Player is win! =(")
            PLAYER_NUM += 1


    


