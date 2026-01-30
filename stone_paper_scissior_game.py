import random
def game(entry,number):
    #for rock and scissior
    if entry=="r" and number==3:
        print("you won")
    elif entry=="s" and number==1:
        print("you lost")   
    # for scissior and paper
    elif entry=="s" and number==2:
        print("you won")
    elif entry=="p" and number==3:
        print("you lost")  
    # for paper and rock
    elif entry=="p" and number==1:
        print("you won")
    elif entry=="r" and number==2:
        print("you lost")  
    else:  
        print("match draw!!")    

number=random.randint(1,3)  
if number==1:
    computer="rock"
elif number==2:
    computer="paper"
elif number==3:
    computer="scissor"
else:
    computer="invalid" 

entry=input("enter your choice:(rock)r,(paper)p,(scissor)s: ").lower()  

if entry=="s":
    user="scissor"
elif entry=="r":
    user="rock"
elif entry=="p":
    user="paper"
else:
    user="invalid"    

if entry=="s" or entry=="p" or entry=="r":
    print("you choose:", user)
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