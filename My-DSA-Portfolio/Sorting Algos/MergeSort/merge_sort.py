class MergeSort:
    def merge(self, arr, low, mid, high):
        left = low
        right = mid + 1
        temp = []
        
        # Merge the two halves into temp
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        # Copy any remaining elements of the left half
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        # Copy any remaining elements of the right half
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        # Copy the sorted elements back into the original array
        for i in range(len(temp)):
            arr[low + i] = temp[i]

    def mergeSort(self, arr, low, high):
        # Base case: if the array has one or no elements, it's already sorted
        if low >= high:
            return
        
        mid = low + (high- low) // 2
        
        # Recursively sort the two halves
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        
        # Merge the sorted halves
        self.merge(arr, low, mid, high)

    def display(self, arr):
        print(arr)

if __name__ == "__main__":
    arr = [1, 8, 9, 3, 7, 5, 2, 2, 1]
    m = MergeSort()
    m.mergeSort(arr, 0, len(arr) - 1)
    m.display(arr)