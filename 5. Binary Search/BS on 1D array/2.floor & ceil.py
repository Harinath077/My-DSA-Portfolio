import bisect

def getFloorAndCeil(arr, n, x):
    # Helper function to calculate floor
    def floor(arr, n, x):
        low = 0
        high = n - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:  # Correct condition for floor
                ans = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans

    # Calculate floor using the helper function
    f = floor(arr, n, x)

    # Calculate ceiling using bisect
    idx = bisect.bisect_left(arr, x)
    c = arr[idx] if idx < n else -1  # Check bounds for ceiling

    return f, c

# Example usage
arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
n = len(arr)
floor, ceil = getFloorAndCeil(arr, n, x)
print(f"Floor: {floor}, Ceil: {ceil}")
