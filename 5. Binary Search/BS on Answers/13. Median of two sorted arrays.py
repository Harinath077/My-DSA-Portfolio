class Solution:
    # Better Brute Force
    def median(nums1: int, nums2: int) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        i, j = 0, 0
        merge = []

        while i < n1 and j < n2:
            if nums1[i] <nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1

        # add the balance elements in nums1 and nums2
        merge.extend(nums1[i:])
        merge.extend(nums2[j:])
        n = n1 + n2
        if n%2 == 0:
            return (merge[(n//2)-1] + merge[n//2]) / 2.0
        else:
            return float(merge[n//2])

    def median(nums1: int, nums2: int) -> float:
        """ Here,and (element1 < 0 or element2 < 0)
        This not neccesary for logic but it helps to little improve optimization
        """
        n1 ,n2 = len(nums1), len(nums2)
        n = n1 + n2
        index2 = n//2
        index1 = index2 - 1
        element1, element2 = -1, -1 
        count = 0 # Tracker
        left, right = 0, 0
        while (left < n1 and right < n2) and (element1 < 0 or element2 < 0) :
            if nums1[left] < nums2[right]:
                if count == index1:
                    element1 = nums1[left]
                if count == index2:
                    element2 = nums1[left]
                count += 1
                left += 1
            else:
                if count == index1:
                    element1 = nums2[right]
                if count == index2:
                    element2 = nums2[right]
                count += 1
                right += 1
                
        # checking remaing elements in nums1 nums2
        while (left < n1)and (element1 < 0 or element2 < 0):
            if count == index1:
                element1 = nums1[left]
            if count == index2:
                element2 = nums1[left]
            count += 1
            left += 1
        while (right < n2)and (element1 < 0 or element2 < 0):
            if count == index1:
                element1 = nums2[right]
            if count == index2:
                element2 = nums2[right]
            count += 1
            right += 1
            
        # check condition:
        if n%2 == 1:
            return float(element2 )
        return float(element1 + element2) / 2.0