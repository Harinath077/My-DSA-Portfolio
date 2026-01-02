class Solution:
    def nth_root(n, m):
        # Edge case when n = 1, return m immediately
        if n == 1:
            return m
        
        # Edge case when m = 1, the root is always 1 for any n
        if m == 1:
            return 1
        
        # Restrict the range to [1, m//2] We can use Range[1 to M] also
        for i in range(1, (m//2) + 1):
            power = i**n
            if power == m:
                return i
            elif power > m:
                break

        return -1
    
    def nth_root(n, m): # This can't handle the overFlow case
        # Edge case when n = 1, return m immediately
        if n == 1:
            return m
        
        # Edge case when m = 1, the root is always 1 for any n
        if m == 1:
            return 1
        
        low, high = 1, m
        while low <= high:
            # Correct midpoint calculation to avoid overflow
            mid = low + (high - low) // 2
            power = mid**n

            if power == m:
                return mid
            elif power < m:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    
    def NthRoot(n: int, m: int) -> int: # This can handle the overFlow case
        def exponentiation(base, exponent, limit):
            ans = 1
            while exponent > 0:
                if exponent % 2 == 1:  # If the exponent is odd, multiply the result by base
                    ans *= base
                    if ans > limit:  # Early exit if the result exceeds the limit
                        return ans
                base *= base  # Square the base
                if base > limit:  # If base exceeds the limit, exit early
                    return ans
                exponent //= 2  # Integer division by 2
            return ans

        low, high = 1, m
        while low <= high:
            mid = (low + high) // 2
            # Use the embedded exponentiation logic to calculate mid^n
            power = exponentiation(mid, n, m)
            
            if power == m:
                return mid
            elif power < m:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# Example usage
n = 3
m = 27
ans = Solution.NthRoot(n, m)
print("The answer is:", ans)