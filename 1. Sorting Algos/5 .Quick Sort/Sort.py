def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        # Find an element greater than or equal to the pivo
        while i <= high - 1 and pivot >= arr[i]: #arr[i] <= pivot:
            i += 1
        # Find an element less than the pivot
        while j >= low + 1 and pivot < arr[j]: #arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[low], arr[j] = arr[j], arr[low]  # Place the pivot at its correct position
    return j


def quick_sort(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)  # Get the pivot index
        quick_sort(arr, low, p_index - 1)   # Sort the left partition
        quick_sort(arr, p_index + 1, high)  # Sort the right partition


def quick_sort_array(arr):
    quick_sort(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    arr = [4, 6, 2, 5, 7, 9, 1, 3]
    print("Before Using Quick Sort:")
    print(arr)

    quick_sort_array(arr)

    print("After Using Quick Sort:")
    print(arr)
