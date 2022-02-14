secret_no = 3
no_guess =0
while no_guess < secret_no :
    guess = int(input('Guess the Number :'))
    no_guess += 1
    if guess == secret_no:
       print("YOU WON!")
       break
else:
    print("Sorry,You lose!")

