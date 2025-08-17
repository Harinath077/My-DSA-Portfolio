class PrimeNumbers:
    number = 69
    def is_prime(self,n):
        if n <= 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
# n = int(input("Enter the number to check the number is prime : "))
m = PrimeNumbers()
print(m.is_prime(69))
# Compare this snippet from Prime%20Number.py:       