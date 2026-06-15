#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
print("MasterMind")

import random
color_Map = {
    "red": "1", "blue": "2", "green": "3",
    "yellow": "4", "orange": "5", "purple": "6"
}

nummer =	{
  1: "Red",
  2: "Blue",
  3: "Green",
    4: "Yellow",
    5: "Orange",
    6: "Purple" 
}
print(nummer[1])    

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
    return [str(random.randint(1, digits)) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    # Count whites by subtracting black and calculating min digit frequency match
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

def show_Secret(mystery):
    print(mystery)

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
           raw = input(f"Attempt {attempt}: ").strip().lower()
parsed = parse_Guess(raw)
valid_Guess = parsed is not None and len(parsed) == 4
if not valid_Guess:
    print("Invalid input. Use 4 colors or digits (e.g. 'red blue green yellow' or '1234').")
if valid_Guess:
    guess = parsed 

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        play_Mastermind()
        again  = input (f"Play again (Y/N) ?").upper()

