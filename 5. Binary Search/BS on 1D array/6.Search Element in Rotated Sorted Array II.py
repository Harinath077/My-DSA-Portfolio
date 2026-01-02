def search(nums, target):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if the middle element is the target
        if nums[mid] == target:
            return True
        
        # Handle duplicates
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
        
        # Check if the left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half must be sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return False

# Example Usage
nums1 = [2, 5, 6, 0, 0, 1, 2]
target1 = 0
S = search(nums1,target1)
# print(search(nums1, target1))  # Output: True

nums2 = [2, 5, 6, 0, 0, 1, 2]
target2 = 3
print(search(nums2, target2))  # Output: False
