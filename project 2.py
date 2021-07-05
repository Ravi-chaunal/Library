import random
randNumber =random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess!=randNumber):
    userGuess=int(input("Enter your guess:"))
    guesses=guesses+1

    if(userGuess==randNumber):
        print("your Guess is right")
    else:
        if(userGuess>randNumber):
            print("Your Guess is wrong Enter the smaller number")
        else:
            print("Your Guess is worng enter the greater number")

print(f"you guessed the number in {guesses} guess ")
with open("highscore.txt",'r')as f:
    highscore=int(f.read())

if(guesses<highscore):
    print("you just broke the high score.")
    with open ("highscore.txt",'w')as f:
        f.write(str(guesses))