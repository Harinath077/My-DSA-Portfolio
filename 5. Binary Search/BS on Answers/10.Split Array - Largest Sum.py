from typing import List
class Solution:
    # Optimal (Binary Search)
    def splitArray(self, nums: List[int], k: int) -> int:
        def subarrayCount(nums,maxSum):
            subarrays = 1
            subarraySum = 0
            for i in range(n):
                if nums[i] + subarraySum <= maxSum:
                    subarraySum += nums[i]
                else:
                    subarrays += 1
                    subarraySum = nums[i]
            return subarrays

        n = len(nums)
        low ,high = max(nums) ,sum(nums)
        while(low <= high):
            mid = (low + high)//2
            subarray_count = subarrayCount(nums,mid)
            if subarray_count > k:
                low = mid + 1
            else: # subarray_count <= k
                high = mid - 1
        return low
    # brute Fore (Linear Search)
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def subarrayCount(nums,maxSum):
            subarrays = 1
            subarraySum = 0
            for i in range(n):
                if nums[i] + subarraySum <= maxSum:
                    subarraySum += nums[i]
                else:
                    subarrays += 1
                    subarraySum = nums[i]
            return subarrays

        n = len(nums)
        low ,high = max(nums) ,sum(nums)
        for maxSum in range(low,high+1):
            subarray_count = subarrayCount(nums,maxSum)
            if subarray_count == k:
                return maxSum
        return low