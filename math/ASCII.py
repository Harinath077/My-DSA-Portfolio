def freq(string): # using Direct Address Table
    freq = [0]*26
    for i in string:
        freq[ord(i)-ord("A")] += 1
    # print like this char --> freq
    for i in range(26):
        # if freq[i] != 0:    
        print(chr(i+65), "-->", freq[i])
    
string = "AABBBCCCCDEFGHIJZFGPDSFDS"
freq(string)

def freq_integers(arr):
    max_val = max(arr)  # Find the maximum integer to size the frequency array
    freq = [0] * (max_val + 1)  # Create a Direct Address Table

    # Count occurrences
    for num in arr:
        freq[num] += 1

    # Print frequencies
    for i in range(len(freq)):
        if freq[i] > 0:
            print(i, "-->", freq[i])

# Example usage
arr = [1, 3, 1, 4, 3, 2, 5, 3, 1, 6, 6, 5, 4, 2]
freq_integers(arr)

from collections import defaultdict

def freq_integers(arr):
    freq = defaultdict(int)

    # Count occurrences
    for num in arr:
        freq[num] += 1

    # Print frequencies
    for key in sorted(freq.keys()):
        print(key, "-->", freq[key])

# Example usage
arr = [-1, -2, 3, -1, 4, 3, -2, -2, 0, 1, 2]
freq_integers(arr)


def freq(arr):
    min_val = min(arr)  # Get the smallest number (offset)
    max_val = max(arr)  # Get the largest number
    offset = -min_val  # Shift all values to be non-negative

    size = max_val - min_val + 1  # Total range of numbers
    freq = [0] * size  # Direct Address Table

    # Count frequencies
    for num in arr:
        freq[num + offset] += 1  # Shift negative numbers to positive indices

    # Print frequency counts
    for i in range(size):
        if freq[i] > 0:
            print(i - offset, "-->", freq[i])  # Convert back to original number

# Example usage
arr = [-5, -1, -5, 2, 2, -1, 7, 8, -5, 0, 0]
freq(arr)

from collections import defaultdict

def freq_integers(arr):
    freq = defaultdict(int)

    # Count occurrences
    for num in arr:
        freq[num] += 1

    # Print frequencies
    for key in sorted(freq.keys()):
        print(key, "-->", freq[key])

# Example usage
arr = [-1, -2, 3, -1, 4, 3, -2, -2, 0, 1, 2]
freq_integers(arr)
