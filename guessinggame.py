name = "Santeri"
guess = ""
numberOfGuesses = 0

while guess != name:
    print("Please, guess my name.")
    guess = input()
    numberOfGuesses += 1

    if guess == name:
        print("Congratulations!")
        print(f"Guesses: {numberOfGuesses}")

    elif guess != name:
        print("Do you want to quit (y/n) ?")
        print(f"Hint: {name[:numberOfGuesses]}")