print("This is Rock , Paper , Scissor Game")



import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='R':
        if you=='S':
            return False
        elif you=='P':
            return True
    elif comp=='P':
        if you=='R':
            return False
        elif you=='S':
            return True
    elif comp=='S':
        if you=='P':
            return False
        elif you=='R':
            return True



print("comp turn : Rock(R) Paper(P) or Scissor(S)?")
randno=random.randint(1,3)
if randno==1:
    comp="R"
elif randno==2:
    comp="P"
elif randno==3:
    comp="S"
you=(input("Your Turn Select : Rock(R) Paper(P) or scissor(S)?"))
a=gameWin(comp,you)

print(f"Computer choice {comp}")
print(f"You choice {you}")

if a==None:
    print("Game is tie !")
elif a:
    print("YOU WIN!")
else:
    print("YOU LOSE!")

