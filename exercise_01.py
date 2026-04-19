import random

def main() -> None:
    min = 0
    max = 100
    num = random.randint(min, max)
    guess = -1
    while num != guess:
        guess = get_user_input(
                f"Guess a number between {min} and {max}: ", min, max)
        if guess == num:
            print("You got it!")
        elif guess > num:
            print("Too high.")
        elif guess < num:
            print("Too low.")

def get_user_input(prompt: str, min: int, max: int) -> int:
    result = 0
    valid = False
    while not valid:
        num_str = input(prompt)
        if num_str.isdigit():
            num = int(num_str)
            if min <= num <= max:
                result = num
                valid = True
    return result

if __name__ == "__main__":
    main()
