import random

def game():
    upper = 1
    lower = 20
    attempts = 0


    player_name = input("enter your name ")
    print(f"\nAlright, {player_name}, I have picked a number between {lower} and {upper}. guess it")

    secretnumber = random.randint(lower, upper)

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secretnumber:
            print("Too low! Try again.")
        elif guess > secretnumber:
            print("Too high! Try again.")
        else:
            print(f"Congrats {player_name} you guessed the number in {attempts} attempts")
            break

if __name__ == "__main__":
    print("Starting...\n")
    game()