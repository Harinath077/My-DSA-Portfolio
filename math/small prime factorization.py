class SPF:
    # Function to compute Smallest Prime Factor (SPF) for all numbers up to max_n
    def sieve_of_eratosthenes(self, max_n):
        spf = list(range(max_n + 1))  # Initialize SPF array
        for i in range(2, int(max_n**0.5) + 1):
            if spf[i] == i:  # i is a prime number
                for multiples in range(i * i, max_n + 1, i):
                    if spf[multiples] == multiples:  # Update only if unset
                        spf[multiples] = i
        return spf

    # Function to compute unique prime factorization using SPF
    def smallPrimeFactorization(self, n, spf):
        unique_factors = []
        while n != 1:
            unique_factors.append(spf[n])  # Add the smallest prime factor
            n //= spf[n]  # Divide n by its smallest prime factor
        return unique_factors  # Return sorted unique factors

# Instantiate the class and compute SPF and prime factorization
obj1 = SPF()
n = 30 #12246
max_n = 2*(10**5 + 1)
spf = obj1.sieve_of_eratosthenes(max_n)  # Precompute SPF array
print(obj1.smallPrimeFactorization(n, spf))  # Compute and print unique prime factors
