import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("You will be guessing a randomly generated number.")
    print("As you progress, the difficulty level will increase.")
    
    level = 1  # starting difficulty level
    
    while True:
        max_range = 10 * level  # difficulty increases by expanding the range
        number_to_guess = random.randint(1, max_range)  # random number within the current range
        attempts = 5  # fixed number of attempts at each level
        
        print(f"\nLevel {level}: Guess the number between 1 and {max_range}. You have {attempts} attempts.")
        
        while attempts > 0:
            try:
                user_guess = int(input("Enter your guess (remaining attempts {attempts}): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if user_guess == number_to_guess:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
                break
            elif user_guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
                
            attempts -= 1

            if attempts == 0:
                print("Sorry, you've run out of attempts. The correct number was {number_to_guess}.")
        
        # Ask if the user wants to play again at the next level
        play_again = input("Do you want to go to the next level? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break
        level += 1  # Increase the difficulty level

if __name__ == "__main__":
    start_game()
