#add import
from question_c import get_miles_per_hour

if __name__ == "__main__":
    try:
        kilometers = int(input("Enter kilometers: ").strip())
        minutes = int(input("Enter minutes: ").strip())
    except ValueError:
        print("Invalid input; please enter integer values.")
    else:
        result = get_miles_per_hour(kilometers, minutes)
        print(result if isinstance(result, str) else f"{result}")
