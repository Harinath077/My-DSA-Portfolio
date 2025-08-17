class All_factors:
    
    def bruteForce(self,n):
        for i in range(1,n+1):
            if n % i == 0:
                print(i,end=" ")
        print()
                
    def optimal(self,n):

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                print(i, end=" ")
                if i * i == n:
                    continue
                print(n // i, end=" ")
        
        
n = 36
m = All_factors()
m.bruteForce(n)
m.optimal(n)

def count_factors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):  # Loop up to sqrt(n)
        if n % i == 0:
            count += 1  # Counting i as a factor
            if i * i != n:  # Avoid counting the same factor twice for perfect squares
                count += 1  # Counting n // i as a factor
    return count

# Example test cases
n = 36
print("Total number of factors:", count_factors(n))  # Output: 9

n = 100
print("Total number of factors:", count_factors(n))  # Output: 9

n = 37  # Prime number
print("Total number of factors:", count_factors(n))  # Output: 2
