import random

def generate_random_number():
    """Generates a random number between 1 and 20."""
    return random.randint(1, 20)

def get_user_guess():
    """Gets user input for a guess."""
    return input("Guess a number between 1 and 20: ")

def check_guess(user_guess, random_number):
    """Checks if the user's guess is correct, too high, or too low."""
    try:
        user_guess = int(user_guess)
        if user_guess < random_number:
            print("Too small")
        elif user_guess > random_number:
            print("Too high!")
        return user_guess
    except ValueError:
        return handle_cheats(user_guess, random_number)

def handle_cheats(user_guess, random_number):
    """Handles cheat codes entered by the user."""
    if user_guess == "s":
        print("The number is:", random_number)
        user_guess = int(input("Guess again: "))
        return check_guess(user_guess, random_number)
    elif user_guess == "x":
        exit()
    elif user_guess == "n":
        return "n"  # Indicate to the main loop to ask about playing again
    return user_guess # If it's not a cheat code, handle as usual.



def play_game():
    """Plays a single round of the number guessing game."""
    random_number = generate_random_number()
    number_of_trials = 0
    user_guess = get_user_guess()

    while user_guess != str(random_number):
        user_guess = check_guess(user_guess, random_number)
        if isinstance(user_guess, int):
            number_of_trials += 1
            user_guess = get_user_guess()
        elif user_guess == "n": # break the inner loop in case user used the n cheatcode
            break


    if user_guess == str(random_number) or isinstance(user_guess, int) and user_guess == random_number :    
        print("Congratulations! You guessed it right.")
        print("Number of trials:", number_of_trials)

    return input("Do you want to play again? (yes/no): ")




def main():
    """Main function to control the game loop."""
    print("Let's play a game")
    start_button = "yes"
    while start_button == "yes":
        start_button = play_game()


if __name__ == "__main__":
    main()
