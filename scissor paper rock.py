'''
1=scissor
0=paper
-1=rock
'''
print('''press: s for scissor
       p for paper
       r for rock ''')
print("Enter end to stop the game")
import random
validanswers=['s','p','r']
wins,loses,draws=0,0,0
while True:
    yourstr=input("enter your choice: ").lower()
    yourdict={'s':1,'p':0,'r':-1}
    if yourstr=='end':
        print("game ended")
        break
    if yourstr not in validanswers:
        print("not a valid choice\ntry again")
        continue

    yourchoice=yourdict[yourstr]
    print("your choice is:",yourstr)
    computeroptions=[1,0,-1]
    computer=random.choice(computeroptions)
    compdict={1:'s',0:'p',-1:'r'}
    print("computer's choice is:",compdict[computer])
    if yourchoice==computer:
            print("draw")
            draws+=1
    else:
        if (yourchoice==1 and computer==0) or (yourchoice==0 and computer==-1) or (yourchoice==-1 and computer==1):
                print("you win")
                wins+=1
        else:
                print("computer wins")
                loses+=1
    print(f"score→ wins:{wins} loses:{loses} draws:{draws}")
