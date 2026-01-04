'''
1=scissor
0=paper
-1=rock
'''
n=int(input("enter number of wins required to win the game: "))
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
                if wins==n:
                      print(f"congratulations your score is {n}\nso you have won the game")
                      break
        else:
                print("computer wins")
                loses+=1
                if loses==n:
                      print(f"sorry computer's score is {n}\nso computer has won the game")
                      break
    print(f"score→ wins:{wins} loses:{loses} draws:{draws}")
