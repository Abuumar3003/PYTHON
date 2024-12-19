def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    """Print all prime numbers in the given range."""
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# Get input from the user
try:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    print(f"Prime numbers between {start} and {end}:")
    print_primes_in_range(start, end)
except ValueError:
    print("Please enter valid integers.")
