from typing import List
class Solution:
    # Brute Forece
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possibleDay(bloomDay,day,m,k):
            count = 0
            no_of_Bdays = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    count += 1
                    if count == k:
                        no_of_Bdays += 1
                        count = 0
                else:
                    count = 0
                    

            if no_of_Bdays  >= m:
                return True
            return False
        # Main func
        n = len(bloomDay)
        if m*k > n: # impossible case
            return -1
        min_ = min(bloomDay)
        max_ = max(bloomDay)

        for day in range(min_ , max_ + 1):
           if possibleDay(bloomDay,day,m,k):
            return day
        return -1

    
# bruteForece with clean code
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMakeBouquets(day: int) -> bool:
            """
            Check if it's possible to make `m` bouquets with `k` flowers each 
            by day `day`.
            """
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

                if bouquets >= m:  # Early exit if we can already make enough bouquets
                    return True

            return bouquets >= m

        # Check if it's impossible to make `m` bouquets
        n = len(bloomDay)
        if m * k > n:
            return -1

        # Binary search for the minimum day
        left, right = min(bloomDay), max(bloomDay)
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                result = mid  # Potential answer found
                right = mid - 1  # Try for a smaller day
            else:
                left = mid + 1  # Increase day to find a valid answer

        return result
