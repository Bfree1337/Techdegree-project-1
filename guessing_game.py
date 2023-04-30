import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    high_score = float('inf')
    play_again = True

    while play_again:
        answer = random.randint(1, 10)
        attempts = 0

        while True:
            try:
                guess = int(input("Take a guess: "))
                attempts += 1

                if guess < 1 or guess > 10:
                    print("Your guess is outside the range of 1-10. Please try again.")
                elif guess < answer:
                    print("It's higher")
                elif guess > answer:
                    print("It's lower")
                else:
                    print("Got it! It took you {} attempts".format(attempts))
                    if attempts < high_score:
                        high_score = attempts
                        print("Congratulations! You've set a new high score of {}!".format(high_score))
                    else:
                        print("The current high score is {} attempts.".format(high_score))

                    while True:
                        play_again_input = input("Would you like to play again? (y/n): ")
                        if play_again_input.lower() == "y":
                            break
                        elif play_again_input.lower() == "n":
                            play_again = False
                            break
                        else:
                            print("Invalid input. Please enter either 'y' or 'n'.")

                    break
            except ValueError:
                print("Oops! That was not a valid number. Please try again.")

    print("Thanks for playing!")

# Kick off the program by calling the start_game function.
start_game()
