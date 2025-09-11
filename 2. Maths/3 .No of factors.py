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