from typing import List
import bisect
class Solution:
    def linearSearch(self,arr,target):
        n =len(arr)
        first = -1
        last = -1
        result = []
        for i in range(n):
            if arr[i] == target:
                if first == -1 :
                    first = i
                last = i
        return [first,last]
    
    def optimal(self,arr,target):
        n = len(arr)
        lowerBound = bisect.bisect_left(arr,target)
        if lowerBound == n or arr[lowerBound] != target:
            return [-1, -1]
        upperBound = bisect.bisect_right(arr,target)
        return [lowerBound ,upperBound-1]
    
    
    def binarySearch(self, arr: List[int], target: int) -> List[int]:
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
            return [-1,-1]
        return [first,binarySearchRight(arr,target)]
    
arr = [5,7,7,8,8,10]
target = 8
obj = Solution()
print(obj.linearSearch(arr,target))
print(obj.optimal(arr,target))
print(obj.binarySearch(arr,target))