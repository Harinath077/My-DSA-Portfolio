class Solution:

    def countPainters(self,boards, time):
        n = len(boards)  # size of array
        painters = 1
        boardsPainter = 0
        for i in range(n):
            if boardsPainter + boards[i] <= time:
                # allocate board to current painter
                boardsPainter += boards[i]
            else:
                # allocate board to next painter
                painters += 1
                boardsPainter = boards[i]
        return painters
    
    # brute Fore (Linear Search)
    def findLargestMinDistance_LS(self,boards, k):
        low = max(boards)
        high = sum(boards)

        for time in range(low, high+1):
            if self.countPainters(boards, time) == k:
                return time
        return low
    # Optimal (Binary Search)
    def findLargestMinDistance_BS(self,boards, k):
        low = max(boards)
        high = sum(boards)
        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            painters = self.countPainters(boards, mid)
            if painters > k:
                low = mid + 1
            else:
                high = mid - 1
        return low


obj = Solution()
arr = [2, 1, 5, 6, 2, 3]
k = 2
print(obj.findLargestMinDistance_LS(arr,k))
print(obj.findLargestMinDistance_BS(arr,k))
