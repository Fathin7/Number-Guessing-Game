import random
print("Number Guessing Game")
number=random.randint(1,10)
chances=0

while chances<5:
    guess=int(input("Enter A Number Between 1 And 10:"))
    if guess==number:
        print("Congrats! You Won!")
        break
    elif guess<number:
        print("Guess Is Too Low, Guess A Number Higher Than",guess)
    else:
        print("Guess Is Too High, Guess A Number Lower Than",guess)
    
    chances=+1

if not chances<5:
    print("You Loose! The Number Is",number)