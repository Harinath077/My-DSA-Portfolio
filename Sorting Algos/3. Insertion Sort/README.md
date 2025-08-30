# Insertion Sort Algorithm

Insertion Sort is a simple, intuitive sorting algorithm that builds the final sorted array one item at a time. It's much like how you would sort a hand of playing cards—picking up one card and inserting it into its correct position among the cards you're already holding.



## How It Works

The algorithm iterates through the input elements, and for each element, it finds its correct position in the sorted part of the array and inserts it there. It does this by shifting all the larger elements one position to the right.

***

## Complexity Analysis

The efficiency of Insertion Sort is highly dependent on the initial order of the elements.

### Time Complexity
* **Worst Case:** $O(n²)$ — This occurs when the array is sorted in descending order, and every element needs to be shifted.
* **Average Case:** $O(n²)$ — This occurs when the elements are in a random, jumbled order.
* **Best Case:** $O(n)$ — This occurs when the array is already sorted. The algorithm just has to iterate through the list once.

### Space Complexity
* **In-Place:** $O(1)$ — Insertion sort requires only a constant amount of additional memory space, making it very space-efficient.

***

## Key Features

**Why choose Insertion Sort?** It's not the fastest algorithm for large datasets, but it has several key advantages in specific scenarios.

* **Adaptive** 🏃‍♂️: Its performance improves if the array is already partially sorted. The number of steps is reduced, making it faster than other simple quadratic algorithms like Bubble Sort or Selection Sort in these cases.
* **Stable** ⚖️: It maintains the relative order of equal elements. For example, if two items have the same key, their original order in the input array will be preserved in the sorted output.
* **Efficient for Small Datasets** ✨: It's one of the fastest algorithms for sorting very small arrays. This quality makes it an excellent choice for being a part of more complex **hybrid sorting algorithms**. For instance, some standard library `sort()` functions switch to Insertion Sort for subarrays smaller than a certain threshold.

***

## Implementations

Here's how you can implement Insertion Sort in Python and Java.

### Python
```python
def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --- Example Usage ---
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)

print(f"Original array: [12, 11, 13, 5, 6]")
print(f"Sorted array: {sorted_arr}")