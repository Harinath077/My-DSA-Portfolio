class Solution:
    @staticmethod
    def findPages(arr, n: int, m: int) -> int:
        def CountStudent(arr,pages):
            student_count = 1
            student_pages = 0
            for pageInBook in arr:
                if student_pages + pageInBook <= pages:
                    student_pages += pageInBook
                else:
                    student_count += 1
                    student_pages= pageInBook
            return student_count
        # Impossible case
        if m > n:
            return -1
        low = max(arr)
        high = sum(arr)
        for i in range(low,high+1):
            student_count = CountStudent(arr,i)
            if student_count == m:
                return i
        return low
    
    def findPages(arr, n: int, m: int) -> int: # brute Force
        def CountStudent(arr,pages):
                student_count = 1
                student_pages = 0
                for pageInBook in arr:
                    if student_pages + pageInBook <= pages:
                        student_pages += pageInBook
                    else:
                        student_count += 1
                        student_pages= pageInBook
                return student_count
        # Impossible case
        if m > n:
            return -1
        low = max(arr)
        high = sum(arr)
        for i in range(low,high+1):
            student_count = CountStudent(arr,i)
            if student_count == m:
                return i
        return low

arr = [25, 46, 28, 49, 24]
m = 4 #no.of.student
n =  len(arr)
print(Solution.findPages(arr,n,m))
