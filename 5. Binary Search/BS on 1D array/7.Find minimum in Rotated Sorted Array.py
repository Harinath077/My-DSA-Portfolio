from typing import List
class Solution:
    # @staticmethod
    def findMin( arr: List[int]) -> int:
        n = len(arr)
        low, high = 0, n - 1
        min_ = float("inf")

        while low <= high:
            mid = (low + high) // 2
            # Left part is sorted
            if arr[low] <= arr[mid]:
                min_ = min(min_, arr[low])
                low = mid + 1
            # Right part is sorted
            else:
                min_ = min(min_, arr[mid])
                high = mid - 1
        return min_
    
    def findMin_Optimized( arr: List[int]) -> int:
        n = len(arr)
        low, high = 0, n - 1
        min_ = float("inf")

        while low <= high:
            mid = (low + high) // 2

            # If the subarray is sorted, update min_ and exit
            if arr[low] <= arr[high]:
                min_ = min(min_, arr[low])
                break

            # Left part is sorted
            if arr[low] <= arr[mid]:
                min_ = min(min_, arr[low])
                low = mid + 1
            # Right part is sorted
            else:
                min_ = min(min_, arr[mid])
                high = mid - 1

        return min_
    
    def lowerBound( arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] < arr[high]:
                high = mid
            else:
                low = mid + 1
        return arr[low]

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = Solution.findMin(arr)
    ans1 = Solution.lowerBound(arr)
    print("The minimum element is:", ans)
    print("The minimum element is:", ans1)