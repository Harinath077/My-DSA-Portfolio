class Solution:
    # like a helper Function
    def findDay(self,weights,capacity):
            n = len(weights)
            days = 1
            load = 0
            for i in range(n):
                if load + weights[i] > capacity:
                    days += 1
                    load = weights[i]
                else:
                    load += weights[i]
            return days
    
    def shipWithinDays(self, weights, days: int) -> int: # Brute Force
        max_ = max(weights)
        summation = sum(weights)
        for capacity in range(max_ , summation+1):
            days_required = self.findDay(weights,capacity)
            if days_required <= days:
                return capacity
        return -1
    
    def shipWithinDays(self, weights, days: int) -> int: # Optimal approach
        # main func
        max_ = max(weights)
        summation = sum(weights)
        ans = -1
        low = max_
        high = summation
        while (low <= high):
            mid = (low+high)//2
            days_required = self.findDay(weights,mid)
            if days_required <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


