"""
This script provides three different approaches to count the number of prime numbers in a given range [L, R]:

1. **Brute Force Approach** - Checks each number individually for primality.
2. **Better Approach (Sieve of Eratosthenes)** - Precomputes primes up to a maximum limit using a sieve.
3. **Optimal Approach (Prefix Sum + Sieve)** - Uses a prefix sum of prime counts to answer queries efficiently.
"""

import math

# Function to check if a number is prime (used in Brute Force approach)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Brute Force Approach
def count_primes_brute_force(L, R):
    count = 0
    for num in range(L, R + 1):
        if is_prime(num):
            count += 1
    return count

# Sieve of Eratosthenes to precompute prime numbers (for Better & Optimal Approaches)
def sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not prime
    for i in range(2, int(math.sqrt(limit)) + 1):
        if prime[i]:
            for j in range(i * i, limit + 1, i):
                prime[j] = False
    return prime

# Better Approach: Using Sieve of Eratosthenes
def count_primes_sieve(L, R, prime):
    count = sum(1 for i in range(L, R + 1) if prime[i])
    return count

# Optimal Approach: Precompute Prefix Sum for Faster Queries
def compute_prefix_sum(prime):
    prefix = [0] * len(prime)
    for i in range(1, len(prime)):
        prefix[i] = prefix[i - 1] + (1 if prime[i] else 0)
    return prefix

def count_primes_prefix(L, R, prefix):
    return prefix[R] - prefix[L - 1]

# Driver Code
def main():
    MAX_LIMIT = 1000000  # Adjust as needed
    prime = sieve(MAX_LIMIT)
    prime_prefix = compute_prefix_sum(prime)
    
    queries = [(1, 20), (20, 50), (100, 200)]
    
    print("Brute Force Approach:")
    for L, R in queries:
        print(f"Count of primes in range [{L}, {R}]:", count_primes_brute_force(L, R))
    
    print("\nBetter Approach (Sieve):")
    for L, R in queries:
        print(f"Count of primes in range [{L}, {R}]:", count_primes_sieve(L, R, prime))
    
    print("\nOptimal Approach (Prefix Sum + Sieve):")
    for L, R in queries:
        print(f"Count of primes in range [{L}, {R}]:", count_primes_prefix(L, R, prime_prefix))

if __name__ == "__main__":
    main()
