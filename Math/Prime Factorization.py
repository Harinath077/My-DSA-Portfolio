from Prime_number import PrimeNumbers 

prime = PrimeNumbers()

def bruteForce(n):
    result = []  # O(log sqrt n)
    for i in range(2, int(n**0.5) + 1):  # O(sqrt(N))
        if n % i == 0 and prime.is_prime(i):  # Checking if i is prime
            result.append(i)
            if n // i != i and prime.is_prime(n // i):  # Ensure unique factors
                result.append(n // i)
    if not result:
        result.append(n)  # If n is prime, return n itself
    return result

def better(n):
    result = []
    for i in range(2, int(n**0.5) + 1):  # O(sqrt(n))
        if n % i == 0:
            result.append(i)
            while n % i == 0:
                n //= i  # Remove all occurrences of i
    if n > 1:  # If any prime factor > sqrt(n) remains
        result.append(n)
    return result

def optimal(n):
    result = []
    i = 2

    # Handle even factor 2 separately
    while n % 2 == 0:
        result.append(2)
        n //= 2

    # Check odd numbers from 3 to sqrt(n)
    while i * i <= n:  # Corrected loop condition
        if n % i == 0:
            result.append(i)
            while n % i == 0:
                n //= i
        i = i + 1 if i == 2 else i + 2  # Increment by 2 after 2 to skip evens

    if n > 1:
        result.append(n)
    
    return result

# Test case
n = 100031

print("Brute Force:", bruteForce(n))
print("Better Approach:", better(n))
print("Optimal Approach:", optimal(n))

""" 
# By chatGPT
from math import isqrt

# Brute Force: Checks all factors and verifies primality
def bruteForce(n):
    result = []
    for i in range(2, int(n**0.5) + 1):  # O(sqrt(n))
        if n % i == 0 and is_prime(i):  # Checking if the factor is prime
            result.append(i)
            if n // i != i and is_prime(n // i):  # Ensure unique factors
                result.append(n // i)
    if not result:
        result.append(n)  # If n is prime, return n itself
    return result

# Improved Approach: Extracts prime factors using division
def better(n):
    result = []
    for i in range(2, int(n**0.5) + 1):  # O(sqrt(n))
        if n % i == 0:
            result.append(i)
            while n % i == 0:  # Remove all occurrences of i
                n //= i
    if n > 1:  # If any prime factor > sqrt(n) remains
        result.append(n)
    return result

# Optimal Approach: Efficient prime factorization with optimized iteration
def optimal(n):
    result = []
    
    # Handle even factor 2 separately
    while n % 2 == 0:
        result.append(2)
        n //= 2
    
    # Check odd numbers from 3 to sqrt(n)
    for i in range(3, isqrt(n) + 1, 2):  # O(sqrt(n)/2)
        while n % i == 0:
            result.append(i)
            n //= i

    # If any prime factor > sqrt(n) remains
    if n > 1:
        result.append(n)
    
    return result

# Helper function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test case
n = 12246
print("Brute Force:", bruteForce(n))
print("Better Approach:", better(n))
print("Optimal Approach:", optimal(n))
 """