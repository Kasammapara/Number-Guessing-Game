secret_no = 8
no_guess =0
limit = 3
while no_guess < limit :
    guess = int(input('Guess the Number :'))
    no_guess += 1
    if guess == secret_no:
       print("YOU WON!")
       break
else:
    print("Sorry,You lose!")

