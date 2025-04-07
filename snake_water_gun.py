'''
 1 for snake
-1 for water
 0 for gun

'''
def game():
    import random
    l=[-1,0,1]
    computer=random.choice(l)
    youstr=input("Enter your choice between (Snake,Water,Gun):").lower()
    youDict={"snake":1,"water":-1,"gun":0}
    if(youstr in youDict):
        you=youDict[youstr]
    
        if(computer==you):
            print("Draw!")
        elif(computer==-1 and you==1):
            print("You Win!")
        elif(computer==-1 and you==0):
            print("You Lose!")
        elif(computer==1 and you==-1):
            print("You Lose!")
        elif(computer==1 and you==0):
            print("You Win!")
        elif(computer==0 and you==-1):
            print("You Win!")
        elif(computer==0 and you==1):
            print("You Lose!")
        else:
            print("Something went Worng")
    else:
        print("Wrong Choice!")

while(True):
    again=input("You want to play this game then choose between YES or NO:").lower()
    if(again=="yes"):
        game()
    elif(again=="no"):
        print("Thank You for playing this game!")
        break
    else:
        print("Wrong Choice")
        break