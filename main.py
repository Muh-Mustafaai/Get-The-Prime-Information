def its_prime(num):  
    if num == 1:
        return False
    for i in range(2, int (num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
def generate_primes(n):
    primes = []
    for i in range(2, n + 1):
        if its_prime(i):
            primes.append(i)
    return primes

num = int(input("Enter a number: "))

if its_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    factors = get_factors(num)
    print(f"Factors of {num} are: {factors}")
    primes = generate_primes(num)

limit = int(input("Enter the limit for prime numbers: "))
print(f"Prime numbers up to {limit} are: {generate_primes(limit)}")
   