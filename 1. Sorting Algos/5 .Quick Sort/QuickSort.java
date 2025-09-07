public class QuickSort {

    // Partition method (Lomuto-like but using Hoare's idea from your Python code)
    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[low];  // Choose first element as pivot
        int i = low;
        int j = high;

        while (i < j) {
            // Move i forward until an element greater than pivot is found
            while (i <= high - 1 && arr[i] <= pivot) {
                i++;
            }
            // Move j backward until an element smaller or equal to pivot is found
            while (j >= low + 1 && arr[j] > pivot) {
                j--;
            }
            // Swap arr[i] and arr[j] if they are in the wrong partition
            if (i < j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Place pivot at its correct position
        int temp = arr[low];
        arr[low] = arr[j];
        arr[j] = temp;

        return j; // pivot index
    }

    // Recursive QuickSort
    private static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pIndex = partition(arr, low, high); // pivot index
            quickSort(arr, low, pIndex - 1);       // Left partition
            quickSort(arr, pIndex + 1, high);      // Right partition
        }
    }

    // Public helper method
    public static void quickSortArray(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    // Test the code
    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        quickSortArray(arr);

        // Print sorted array
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
