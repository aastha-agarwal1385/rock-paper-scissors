import random
def game(entry,number):
    #for rock and scissior
    if entry=="r" and number==3:
        return "you won this round"
    elif entry=="s" and number==1:
        return "you lost this round"   
    # for scissior and paper
    elif entry=="s" and number==2:
        return "you won this round"
    elif entry=="p" and number==3:
        return "you lost this round"  
    # for paper and rock
    elif entry=="p" and number==1:
        return "you won this round"
    elif entry=="r" and number==2:
        return "you lost this round"  
    else:  
        return "it's a tie this round!!"    

#INTRODUCTION AND RULES TO PLAY
print("Hi there,we are going to play stone-paper-scissor ")
print("Make your choice wisely!! \n")
print("Rules:")
print("Game has 5 rounds.")
print("you will have 5 chances to make a choice.")
print("You will win if you win 3 or more rounds.")
count = 0
for i in range(1,6):
    print("\n\nround ",i)
    number=random.randint(1,3)  
    computer_map={1:"rock",2:"paper",3:"scissor"}
    computer=computer_map[number]

    entry=input("enter your choice:(rock)r,(paper)p,(scissor)s: ").lower()  
    user_map={"s":"scissor","r":"rock","p":"paper"} 

    if entry=="s" or entry=="p" or entry=="r":
        print("you choose:", user_map[entry])
        i+=1
    else:
        print("invalid entry!!")
        print("please choose:(rock)r,(paper)p,(scissor)s ") 
        print("we will not count this round")
        exit()  

    if number==1 or number==2 or number==3:
        print("computer choose: ", computer)
    else:
        print("invalid choice made by the computer")
        print("please try again!!")

    result=game(entry,number) 
    if result==None:
        print("invalid") 
    else:     
        print(result)         

