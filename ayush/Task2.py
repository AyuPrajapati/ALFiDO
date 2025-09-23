import random
def guess_game():
    number = random.randint(1,100)
    attempts = 0
    while True:
        attempts += 1
        guess = input("Guess a number between 1 and 100: ")
        if not guess.isdigit():
            print("Please enter a valid integer.")
            continue
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Your guess is out of bounds.")
        elif guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
if __name__ == "__main__":
    guess_game()
