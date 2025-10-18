#add import
# ...existing code...
#add import
import math

def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    # 2) Tests
    tests = {4: False, 5: True, 11: True}
    for value, expected in tests.items():
        result = is_prime(value)
        print(f"is_prime({value}) -> {result} (expected {expected})")
        assert result == expected, f"Test failed for {value}"

    # 3) Interactive loop
    while True:
        s = input("Enter an integer to test for prime (or 'q' to quit): ").strip()
        if s.lower() in ("q", "quit", "exit"):
            print("Quitting.")
            break
        try:
            n = int(s)
        except ValueError:
            print("Please enter a valid integer or 'q' to quit.")
            continue
        print(f"{n} is {'prime' if is_prime(n) else 'not prime'}.")