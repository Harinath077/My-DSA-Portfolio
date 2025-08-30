class Solution:
    def insertionSort(self, arr):
        # Traverse trough 1 --> n-1
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            # Move elements of arr[0..i-1], that are greater than key,
            # to one position ahead of their current position
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
# Driver code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Unsorted array is:", arr)
    solution = Solution()
    sorted_arr = solution.insertionSort(arr)
    print("Sorted array is:", sorted_arr)