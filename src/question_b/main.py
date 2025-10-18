# ...existing code...
#add import
import random

def play_game():
    secret = random.randint(1, 5)
    print("I have chosen a number between 1 and 5. Try to guess it!")
    while True:
        s = input("Enter your guess (or 'q' to quit this game): ").strip()
        if s.lower() in ("q", "quit", "exit"):
            print("Exiting current game.")
            return
        try:
            guess = int(s)
        except ValueError:
            print("Please enter a valid integer or 'q' to quit.")
            continue
        if guess == secret:
            print(f"Congratulations! {guess} is correct.")
            return
        else:
            print("Incorrect, try again.")

if __name__ == "__main__":
    while True:
        choice = input("Enter 'p' to play, or 'q' to quit: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Quitting program.")
            break
        if choice in ("p", "play", ""):
            play_game()
            # after a finished game, loop continues until user quits
            continue
        print("Unknown option. Enter 'p' to play or 'q' to quit.")