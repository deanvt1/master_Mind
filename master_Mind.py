#!/bin/python3
# MasterMind
# ICTROCN

import random

print("MasterMind")

color_Map = {
    "red": "1",
    "blue": "2",
    "green": "3",
    "yellow": "4",
    "orange": "5",
    "purple": "6",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
}


nummer = {
    1: "Red",
    2: "Blue",
    3: "Green",
    4: "Yellow",
    5: "Orange",
    6: "Purple",
}


def parse_Guess(guess):
    parts = guess.strip().lower().split()
    result = []

    for part in parts:
        if part in color_Map:
            result.append(color_Map[part])
        else:
            return None

    return result


def generate_Code(length=4, digits=6):
    return [
        str(random.randint(1, digits))
        for _ in range(length)
    ]


def get_Feedback(secret, guess):
    black_Pegs = sum(
        s == g for s, g in zip(secret, guess)
    )

    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(
        min(secret_Counts.get(d, 0), guess_Counts.get(d, 0))
        for d in guess_Counts
    )

    return black_Pegs, white_Pegs


def show_Secret(mystery):
    user = "Admin"
    password = "P@ssw0rd"

    userinput = input("Your username: ")
    passwordinput = input("Your password: ")

    if userinput == user and passwordinput == password:
        print(mystery)
    else:
        print("Access denied!")


def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code (1-6). You have 10 attempts.")

    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        valid_Guess = False
        guess = None
        black = 0
        white = 0

        while not valid_Guess:
            raw = input(
                f"Attempt {attempt}: "
            ).strip().lower()

            if raw == "login":
                show_Secret(secret_Code)
                continue

            parsed = parse_Guess(raw)
            valid_Guess = (
                parsed is not None
                and len(parsed) == 4
            )

            if not valid_Guess:
                print(
                    "Invalid input. Use 4 colors or digits "
                    "(e.g. 'red blue green yellow' or '1234')."
                )

        guess = parsed

        black, white = get_Feedback(
            secret_Code, guess
        )

        print(
            "Black pegs (correct position): "
            f"{black}, White pegs (wrong position): {white}"
        )

        if black == 4:
            print(
                "Congratulations! You guessed the code: "
                f"{''.join(secret_Code)}"
            )
            return

    print(
        "Sorry, you've used all attempts. "
        f"The correct code was: {''.join(secret_Code)}"
    )


if __name__ == "__main__":
    again = "Y"

    while again == "Y":
        play_Mastermind()
        again = input("Play again (Y/N)? ").upper()

