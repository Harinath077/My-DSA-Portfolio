from Prime_number import PrimeNumbers
prime = PrimeNumbers()
class SevieOfEratosthenes:
    def brtueForce(self,n):
        if n <= 1:
            return []
        result = []
        for i in range(2,n+1):
            if prime.is_prime(i):
                result.append(i)
        return result
    
    
    def sieve_of_eratosthenes(self,n):
        sieve = [True] * (n + 1)
        # precomputing process
        for i in range(2, n + 1):
            if sieve[i]:
                for multiples in range(i * 2, n + 1, i):
                    sieve[multiples] = False
        #prining all primes from range ( i -> n )
        for i in range(2, n + 1):
            if sieve[i]:
                print(i, end=' ')
    
    # Optimized version of sieve_of_eratosthenes just by changing the range of multiples and starting point of i
    def sieve_of_eratosthenes(self,n):
        sieve = [True] * (n + 1)
        # precomputing process
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                # optimizing the process
                # we dont need to start from i^2     for multiples in range(i * 2, n + 1, i):
                for multiples in range(i * i, n + 1, i):
                    sieve[multiples] = False
        #prining all primes from range ( i -> n )
        primes = [i for i in range(2, n + 1) if sieve[i]]  # Collect all primes
        return primes

s = SevieOfEratosthenes()
n = 30
print(s.brtueForce(n))
print(s.sieve_of_eratosthenes(n))