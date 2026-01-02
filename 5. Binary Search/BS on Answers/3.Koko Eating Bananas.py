import math
class Solution:
    def minimumRateToEatBananas(self,piles, h):
        # Find the maximum value in the list
        maxi = max(piles)

        # Iterate through possible hourly rates to find the minimum rate
        for hourly in range(1, maxi + 1):
            # Calculate total hours needed for the current rate
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / hourly)

            # Check if the total hours are within the allowed time
            if total_hours <= h:
                return hourly

        # If no solution is found, return the maximum rate (fallback)
        return maxi
    
    import math

    def minimumRateToEatBananas(self,piles, h):
        # Binary search for the minimum eating rate
        low, high = 1, max(piles)
        ans = -1  # Initialize answer variable

        while low <= high:
            mid = (low + high) // 2
            # Calculate total hours required with the current eating rate
            total_hours = sum(math.ceil(pile / mid) for pile in piles)
            
            if total_hours <= h:
                ans = mid  # Store the current valid rate as the answer
                high = mid - 1  # Try a smaller eating rate
            else:
                low = mid + 1  # Increase the eating rate
                
        return low # ans
    
    
piles = [3,6,7,11]
h = 8
obj = Solution()
print(obj.minimumRateToEatBananas(piles,h))