#no.of frequency
class Math_1:
    
    def no_frequency_A(self,s):
        arr = [0]*26
        n = len(s)
        for i in range(n):
            arr[ord(s[i]) - 65] += 1
        for i in range(26):
            char = chr(i + 65)
            print(f"{char} --> {arr[i]}")

    def no_frequency_a(self,s):
        arr = [0]*26
        n = len(s)
        for i in range(n):
            arr[ord(s[i]) - ord("a")] += 1
        for i in range(26):
            char = chr(i + 65)
            print(f"{char} --> {arr[i]}")
    def count_frequency(self,nums):
        # Create a frequency array for numbers -10 to 10 (21 slots)
        freq = [0] * 21

        # Count the occurrences of each number
        for num in nums:
            freq[num + 10] += 1  # Offset -10 to index 0, -9 to index 1, ....., 10 to index 20

        # Print the frequencies
        for i in range(-10, 11):  # Iterate from -10 to 10
            print(f"{i} --> {freq[i + 10]}")
    def count_digit(self,n):
        count = 0
        while n:
            n = n // 10
            count += 1
        return f"no.of counts : {count}"
    def reverse_int(self,N):
        original = N
        reverse = 0
        while N:
            reverse *= 10
            reverse += N%10
            N = N // 10
        return f"reverse of this {original} is {reverse}"
    def is_palindrom(self,N):
        if N < 0:
            return False
        original = N
        reverse = 0
        while N:
            reverse *= 10
            reverse += N%10
            N = N // 10
        return original == reverse
            
nums = [-10, -5, -10, 0, 5, 10, 5, -1, 0, 10]
n = 56789
m = Math_1()
N = 121
#m.count_frequency(nums)
print(m.count_digit(n))
print(m.reverse_int(N))
print(m.is_palindrom(N))




        