import random

# determines outcome of single round
def game(entry, number, user_map, computer_map):
    user_choice = user_map[entry]
    computer_choice = computer_map[number]

    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissor") \
         or (user_choice == "scissor" and computer_choice == "paper") \
         or (user_choice == "paper" and computer_choice == "rock"):
        return "won"
    else:
        return "lose"


#INTRODUCTION AND RULES TO PLAY
print("Hi there,we are going to play stone-paper-scissor ")
print("Make your choice wisely!! \n")
print("Rules:")
print("Game has 5 rounds.")
print("you will have 5 chances to make a choice.")
print("You will won if you won 3 or more rounds.")

count_round=1
won = 0
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
    result=game(entry, number, user_map, computer_map) 
    if result == "won":
        print("you won this round")
        won += 1
    elif result == "lose":
        print("you lost this round")
        lose += 1
    else:
        print("it's a tie this round!!")

    count_round +=1     
 
 # FINAL RESULT
print("\n\nFinal Result:")
print("Your wins:", won)
print("Computer wins:", lose)   
if won > lose:
    print("You won the game")
elif lose > won:
    print("You lost the game")
else:
    print("The game is a draw")
