class SumOFEvenAndOdd_index:
    def Approach1(self, n):
        def findX(n):
            if n % 2 == 0:
                x = n // 2
            else:
                x = n // 2 + 1
            return x

        def odd(n):
            x = (n+1)//2
            return x ** 2

        def even(n):
            x = findX(n)
            return (n*(n+1))//2 - x ** 2

        return odd(n), even(n) 
    
    
    
    
    def approach2(self, n):
        # Count of odd and even numbers
        odd_count = (n + 1) // 2  # Number of odd numbers
        even_count = n // 2       # Number of even numbers

        # Using the formulas
        odd_sum = odd_count ** 2
        even_sum = even_count * (even_count + 1)

        return odd_sum, even_sum
m = SumOFEvenAndOdd_index()
print(m.approach2(n = 10))
print(m.Approach1(n = 10))

def sum_of_even_numbers_loop(n):
    sum_even = 0
    for i in range(n):
        sum_even += (2 * (i + 1))  # Generating even numbers using 2(i+1)
    return sum_even

# Example usage
n = int(input("Enter the number of even numbers: "))
print("Sum of first", n, "even natural numbers is:", sum_of_even_numbers_loop(n))
