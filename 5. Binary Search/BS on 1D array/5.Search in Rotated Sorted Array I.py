class Solution:
    @staticmethod
    def liner(nums,target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    def search(nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid

            # Determine which half is sorted
            if nums[low] <= nums[mid]:  # Left half is sorted
                if nums[low] <= target < nums[mid]:  # Target in the left half
                    high = mid - 1
                else:  # Target in the right half
                    low = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[high]:  # Target in the right half
                    low = mid + 1
                else:  # Target in the left half
                    high = mid - 1

        return -1  # Target not found

# Test Case 1
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(Solution.search(nums, target))  # Output: 4

# Test Case 2
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(Solution.liner(nums, target))  # Output: -1

# Test Case 3
nums = [1]
target = 0
print(Solution.search(nums, target))  # Output: -1
