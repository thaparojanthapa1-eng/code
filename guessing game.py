from random import randint
n=int(input("Put the upper limit of the guess: "))
rightanswer=randint(1,n)
attempts=int(input("Put the maximum number of attempts available: "))
g=attempts
while attempts!=0:
    num=int(input("Enter your guess: "))
    if num>n or num<1:
        print("Invalid guess")
    else:
        if num==rightanswer:
            print('''\t>>> >>> >>>   PERFECT guess!   <<< <<< <<<\n
\t>>> >>> >>>   WELL DONE!   <<< <<< <<<\n
\t>>> >>> >>>   YOU DID IT!   <<< <<< <<<\n''')
            break
        elif num>rightanswer:
            print("A little lower")
            attempts-=1
            print(f"{attempts} guess left")
        else:
            print("A little higher")
            attempts-=1
            print(f"{attempts} guess left")
else:
    print(f"Sorry!\nYou couldn't guess the number in {g} tries")
