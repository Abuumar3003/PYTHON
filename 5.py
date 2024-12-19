def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def is_palindrome(num):
    return str(num) == str(num)[::-1]
def next_palindrome(num):
    num += 1
    while not is_palindrome(num):
        num += 1
    return num
def check_prime_and_next_palindrome(num):
    if is_prime(num):
        print(f"{num} is a prime number.")
        next_pal = next_palindrome(num)
        print(f"The next palindrome number after {num} is {next_pal}.")
    else:
        print(f"{num} is not prime.")
number = 11
check_prime_and_next_palindrome(number)
