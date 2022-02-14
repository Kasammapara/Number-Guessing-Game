secret_no = 3
no_guess = 0
while no_guess < 3 :
    guess = int(input("Guess The Number: "))
    no_guess += 1
    if guess == secret_no :
      print("You Won!")
    break
else:
  print("Sorry, You Lose!")
