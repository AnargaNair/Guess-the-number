import random
number=random.randint(1,10)

player_name= input("Hey! What is your name?")
number_of_guesses=0
input("Ok!" +player_name+" I will think of a number between 1 to 10. You try and guess the number in 5 tries")

while number_of_guesses<6:
    guess=int(input())
    number_of_guesses+=1
    if guess<number:
        print("Your guess is too low.")
    if guess>number:
        print("Your guess is too high.")      
    if guess== number:
        break 

if guess==number:
    print("You guessed the number in",number_of_guesses, "tries")

else:
    print("You could not guess the number.The number is ",number," Better luck next time!")    
