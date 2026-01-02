class Solution:
    def singleNonDuplicate(self, nums) -> int:
        n = len(nums)
        # Edage Cases
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        # Binary Search
        low, high = 1, n-2
        while(low <= high):
            mid = (low + high)//2
            # If nums[mid] is the single element:
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            # We are in the left:
            if (not mid&1 and nums[mid] == nums[mid+1]) or ( mid&1 and nums[mid] == nums[mid-1]):
                # Eliminate the left half:
                low = mid + 1
            else: # (mid&1 and nums[mid] == nums[mid+1]) or ( not mid&1 and nums[mid] == nums[mid-1]):
            # Eliminate the right half:
                high = mid - 1
                
                

        # Dummy return statement:
        return -1

obj = Solution()
nums = [3, 3 ,4 ,4 ,5 , 5 ,6 ,7 ,7 , 8, 8]
print(obj.singleNonDuplicate(nums))

        
            
            
        