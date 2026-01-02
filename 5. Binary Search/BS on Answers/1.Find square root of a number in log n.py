import math
class Solution:


    def floorSqrt(n: int) -> int:
        return math.floor(math.sqrt(n))
        
        
    def floorSqrt(self, n): 
        low = 1
        high = n // 2
        ans = -1
        while low <= high:
            mid = low + (high - low )//2
            
            val = mid * mid 
            if val == n:
                return mid
            elif val <= n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return high # or ans  
    
    def BruteForce(self,n):
        ans = 0
        for i in range(1,n+1):
            val = i * i
            if val <= n:
                ans = i
        return ans
    
    def floorSqrt(n: int) -> int:
        return int(n ** 0.5)
