class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        n = len(arr)
        low ,high = 0 ,n-1
        while (low <= high):
            mid = (low + high)//2
            missing = arr[mid] - (mid+1)

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return high+k+1 # or low + k

    def bruteForce(self,arr,k):
        n = len(arr)
        for i in range(n):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k
    
arr = [2,3,4,7,11]
k = 5
obj = Solution()
print(obj.bruteForce(arr,k))
# print(obj.findKthPositive(arr,k))