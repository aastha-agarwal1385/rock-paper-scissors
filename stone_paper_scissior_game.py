import random
def game(entry,number):
    #for rock and scissior
    if entry=="r" and number==3:
        return "you won"
    elif entry=="s" and number==1:
        return "you lost"   
    # for scissior and paper
    elif entry=="s" and number==2:
        return "you won"
    elif entry=="p" and number==3:
        return "you lost"  
    # for paper and rock
    elif entry=="p" and number==1:
        return "you won"
    elif entry=="r" and number==2:
        return "you lost"  
    else:  
        return "match draw!!"    

number=random.randint(1,3)  
computer_map={1:"rock",2:"paper",3:"scissor"}
computer=computer_map[number]


entry=input("enter your choice:(rock)r,(paper)p,(scissor)s: ").lower()  
user_map={"s":"scissor","r":"rock","p":"paper"} 

if entry=="s" or entry=="p" or entry=="r":
    print("you choose:", user_map[entry])
else:
    print("invalid entry!!")
    print("please choose:(rock)r,(paper)p,(scissor)s ")   

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