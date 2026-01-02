import math
class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        n = len(nums)
        max_ = max(nums)
        low ,high = 1, max_
        ans = -1
        while(low <= high):
            mid = (low + high)//2
            sum_ = sum(math.ceil(n/mid) for n in nums)
            if sum_ <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    
    def smallestDivisor(self, nums, threshold: int) -> int:
        n = len(nums)
        max_ = max(nums)
        for i in range(1, max_+1):
            sum_ = sum(math.ceil(n/i) for n in nums)
            if sum_ <= threshold:
                return i 
        return -1 

nums = [1,2,5,9]
threshold = 6
obj = Solution()
print((obj.smallestDivisor(nums,threshold)))
