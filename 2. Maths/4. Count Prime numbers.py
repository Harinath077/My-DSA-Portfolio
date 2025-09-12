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


