# Insertion Sort Notes

## Time Complexity
1. **Worst Case (descending sorted)** → `O(n²)`  
2. **Best Case (already sorted)** → `O(n)`  

---

## Why Use Insertion Sort?

- **Adaptive**  
  Steps get reduced if the array is already sorted  
  *(i.e., the number of swaps is reduced compared to bubble sort).*

- **Stable Sorting Algorithm**  
  Maintains the relative order of equal elements.

- **Good for Smaller Values of `n`**  
  Works well when the array is partially sorted.  
  Often used as part of **hybrid sorting algorithms**.

---

## Insertion Sort Implementations

### **Python**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example
arr = [12, 11, 13, 5, 6]
print("Sorted array:", insertion_sort(arr))
