import random

class NumberGuessGame:
    def __init__(self, lower_limit, upper_limit):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.secret_number = random.randint(lower_limit, upper_limit)
        self.attempts = 0

    def guess(self, number):
        self.attempts += 1
        if number < self.secret_number:
            return "Higher"
        elif number > self.secret_number:
            return "Lower"
        else:
            return f"Congratulations! You guessed the number in {self.attempts} attempts."

    def get_attempts(self):
        return self.attempts

    def get_limits(self):
        return self.lower_limit, self.upper_limit

def main():
    print("Welcome to the Number Guessing Game!")
    lower_limit, upper_limit = 1, 100  # You can set your desired limits.

    game = NumberGuessGame(lower_limit, upper_limit)

    while True:
        lower_limit, upper_limit = game.get_limits()
        print(f"Guess a number between {lower_limit} and {upper_limit}: ")
        try:
            guess = int(input())
            result = game.guess(guess)
            print(result)

            if "Congratulations" in result:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Total attempts: {game.get_attempts()}")

if __name__ == "__main__":
    main()
