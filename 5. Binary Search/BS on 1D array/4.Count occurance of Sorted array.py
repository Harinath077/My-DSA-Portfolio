import bisect
class Solution:
    def FirstLast(self,arr,target):
        n = len(arr)
        def binarySearchLeft(arr,target):
            low, high = 0, n-1
            first = -1
            while(low <= high):
                mid = (low+high)//2
                if arr[mid] == target:
                    first = mid
                    high = mid - 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first
        
        def binarySearchRight(arr,target):
            low, high = 0, n-1
            last = -1
            while(low <= high):
                mid = (low+high)//2
                if arr[mid] == target:
                    last = mid
                    low = mid + 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last
        first = binarySearchLeft(arr,target)
        if first == -1:
            return 0
        last = binarySearchRight(arr,target)
        
        return last - first + 1
    
    def lowerAndUpper(self,arr,target):
        # Find the first position where target could appear
        left = bisect.bisect_left(arr, target)
        # Find the position just after the last occurrence of target
        right = bisect.bisect_right(arr, target)
        # Difference gives the count of target in the array
        return right - left
    
obj = Solution()
arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
print(obj.FirstLast(arr,target))
print(obj.lowerAndUpper(arr,target))