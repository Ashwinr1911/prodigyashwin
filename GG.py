import random

def main():
    min_range = 1
    max_range = 100
    total_rounds = 3
    score = 0

    print("Welcome to Guess the Number Game!")
    print("You have to guess a number between 1 and 100.")

    for current_round in range(1, total_rounds + 1):
        target_number = random.randint(min_range, max_range)
        attempts = 0
        max_attempts = 10

        print("\nRound", current_round, "of", total_rounds)
        print("Round Score:", score)

        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == target_number:
                print("Congratulations! You guessed the correct number in", attempts, "attempts.")
                round_score = calculate_round_score(attempts)
                score += round_score
                print("Round Score:", round_score)
                break
            elif guess < target_number:
                print("Your guess is lower than the target number.")
            else:
                print("Your guess is higher than the target number.")

            if attempts >= max_attempts:
                print("Sorry, you have reached the maximum number of attempts. The correct number was:", target_number)
                break

    print("\nGame Over!")
    print("Total Score:", score)

def calculate_round_score(attempts):
    if attempts <= 3:
        return 10
    elif attempts <= 6:
        return 5
    else:
        return 1

if __name__ == '__main__':
    main()
