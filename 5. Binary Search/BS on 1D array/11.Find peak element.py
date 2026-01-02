class Solution:
    def findPeakElement(self,arr):
        n = len(arr)
        # Edage case
        if n == 1 :
            return 0
        if arr[0] > arr[1]:
            return 0
        if arr[-1] > arr[-2]:
            return n-1
        # Binary Search
        low = 1
        high = n-2
        while(low <= high):
            mid = low + (high-low)//2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            # Peak in Increasing
            if arr[mid] > arr[mid-1]:
                low = mid + 1
            else: #decreasing or special case mid point
                high = mid -1
        return -1
obj = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
classic_example = [1, 5, 1, 2, 1]
ans = obj.findPeakElement(arr)
res = obj.findPeakElement(classic_example)
print("The peak is at index:", ans)
print("The peak is at index:", res)
        