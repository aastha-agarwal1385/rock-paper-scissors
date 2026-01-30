import random

# determines outcome of single round
def game(entry,number):
    #for rock and scissior
    if entry=="r" and number==3:
        return "won"
    elif entry=="s" and number==1: 
        return "lose" 

    # for scissior and paper
    elif entry=="s" and number==2:
        return "won"
    elif entry=="p" and number==3:
        return "lose" 

    # for paper and rock
    elif entry=="p" and number==1:
        return "won"
    elif entry=="r" and number==2:
        return "lose"  
    else:  
        return "tie"    

#INTRODUCTION AND RULES TO PLAY
print("Hi there,we are going to play stone-paper-scissor ")
print("Make your choice wisely!! \n")
print("Rules:")
print("Game has 5 rounds.")
print("you will have 5 chances to make a choice.")
print("You will win if you win 3 or more rounds.")

count_round=1
win = 0
lose = 0
while count_round<6:
    print("\n\nround ",count_round)

    #computer and user's choice
    number=random.randint(1,3)  
    computer_map={1:"rock",2:"paper",3:"scissor"}
    entry=input("enter your choice:(rock)r,(paper)p,(scissor)s: ").lower()  
    user_map={"s":"scissor","r":"rock","p":"paper"} 

    #cheak condition of valid entry
    if entry not in user_map:
        print("invalid entry!!")
        print("please choose:(rock)r,(paper)p,(scissor)s ") 
        print("we will not count this round") 
        continue

    #displays choices
    print("you choose:", user_map[entry]) 
    print("computer choose: ", computer_map[number])
    

    #evalute each round
    result=game(entry,number) 
    if result == "won":
        print("you won this round")
        win += 1
    elif result == "lose":
        print("you lost this round")
        lose += 1
    else:
        print("it's a tie this round!!")

    count_round +=1     
 
 # FINAL RESULT
print("\n\nFinal Result:")
print("Your wins:", win)
print("Computer wins:", lose)   
if win > lose:
    print("You won the game")
elif lose > win:
    print("You lost the game")
else:
    print("The game is a draw")
