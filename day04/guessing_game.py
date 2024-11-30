print("Let's play a game")

#Initiate the game
start_botton = "yes"
while start_botton == "yes":
    import random
    if start_botton == "no":
        exit()
#random numbers
    random_number = random.randint(1, 20)
    number_of_trials = 0
    #User guess and cheats
    user_guess = input("Guess a number between 1 and 20: ")
    while user_guess != str(random_number):
        try:
            user_guess = int(user_guess)
            number_of_trials = number_of_trials + 1
            if user_guess < random_number:
                print("Too small")
            else:
                print("Too high!")
            user_guess = input("Guess again: ")
        except ValueError:
            number_of_trials = number_of_trials +1
            if user_guess == "s":
                print("The number is:", random_number)
                user_guess = int(input("Guess again: "))
                if user_guess == random_number:
                    print("Congratulations! You guessed it right.")
                    print("Number of trials:", number_of_trials)
                    start_botton=input("Do you want to play again? (yes/no): ")
                    break
                elif user_guess < random_number:
                    print("Too small")
                else:
                    print("Too high!")
            elif user_guess == "x":
                exit()
            elif user_guess == "n":
                start_botton=input("Do you want to play again? (yes/no): ")
                break

    if user_guess == str(random_number):    
        print("Congratulations! You guessed it right.")
        print("Number of trials:", number_of_trials)
        start_botton=input("Do you want to play again? (yes/no): ")



