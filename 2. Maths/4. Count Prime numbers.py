import math
class Bruteforce:
    def is_primes(self,n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def count_primes_brute(self,queries):
        results = []
        for L, R in queries:
            count = 0
            for num in range(L, R + 1):
                if self.is_primes(num):
                    count += 1
            results.append(count)
        return results

class Better:
    def sieve(self,N):
        prime = [1] * (N + 1)
        prime[0] = prime[1] = 0  # 0 and 1 are not prime
        
        for i in range(2, int(N**0.5) + 1):
            if prime[i]:
                for j in range(i * i, N + 1, i):
                    prime[j] = 0
        
        return prime

    def count_primes_better(self,queries, N=10**6):
        prime = self.sieve(N)
        results = []
        for L, R in queries:
            count = sum(prime[L:R+1])
            results.append(count)
        return results


