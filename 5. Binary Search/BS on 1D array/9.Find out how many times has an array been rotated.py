class Solution:
    @staticmethod
    def findRotation(arr):
        n = len(arr)
        low , high = 0, n-1
        ans = float("inf")
        index = 0
        while(low <= high):
            mid = (low + high)//2
            # If the subarray is already sorted, update ans and break
            if arr[low] <= arr[high]:
                if arr[low] < ans:
                    index = low
                    ans = arr[low]
                    break
            # Left off is sorted
            if arr[low] <= arr[mid]:
                if arr[low] < ans:
                    index = low
                    ans = arr[low]
                low = mid + 1
            else: # Right off is sorted
                if arr[mid] < ans:
                    index = mid
                    ans = arr[mid]
                high = mid - 1
        return index
    
    # Follow up Array contains Duplicates elements
    def Duplicate(arr):
        n = len(arr)
        low , high = 0, n-1
        ans = float("inf")
        index = 0
        while(low <= high):
            mid = (low + high)//2
            
            # Edage case Duplicates
            if arr[low] == arr[mid] == arr[high]:
                high -= 1
                low += 1
                continue
            # If the subarray is already sorted, update ans and break
            if arr[low] <= arr[high]:
                if arr[low] < ans:
                    index = low
                    ans = arr[low]
                    break
            
            # Left off is sorted
            if arr[low] <= arr[mid]:
                if arr[low] < ans:
                    index = low
                    ans = arr[low]
                low = mid + 1
            else: # Right off is sorted
                if arr[mid] < ans:
                    index = mid
                    ans = arr[mid]
                high = mid - 1
        return index
                    
if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    arr_d = [5 ,5 ,6 ,1 ,2 ,3 ,3 ,5]
    ans = Solution.findRotation(arr)
    ans_d = Solution.Duplicate(arr)
    
    print(ans)
    print(ans_d)
    