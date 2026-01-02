import heapq
class Solution:
    # Brute Force
    def minimiseMaxDistance_BF(arr, k):
        n = len(arr)  # size of array
        howMany = [0] * (n - 1)

        # Pick and place k gas stations:
        for gasStations in range(1, k + 1):
            # Find the maximum section and insert the gas station:
            maxSection = -1
            maxInd = -1
            for i in range(n - 1):
                diff = arr[i + 1] - arr[i]
                sectionLength = diff / (howMany[i] + 1)
                if sectionLength > maxSection:
                    maxSection = sectionLength
                    maxInd = i
            # insert the current gas station:
            howMany[maxInd] += 1

        # Find the maximum distance i.e. the answer:
        maxAns = -1
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            sectionLength = diff / (howMany[i] + 1)
            maxAns = max(maxAns, sectionLength)
        return maxAns

    # better approach Using Priorty Queue
    def minimiseMaxDistance_BT(arr, k):
        n = len(arr)  # size of array.
        howMany = [0] * (n - 1)
        pq = []

        # insert the first n-1 elements into pq
        # with respective distance values:
        for i in range(n - 1):
            heapq.heappush(pq, ((-1)*(arr[i + 1] - arr[i]), i))

        # Pick and place k gas stations:
        for gasStations in range(1, k + 1):
            # Find the maximum section
            # and insert the gas station:
            tp = heapq.heappop(pq)
            secInd = tp[1]

            # insert the current gas station:
            howMany[secInd] += 1

            inidiff = arr[secInd + 1] - arr[secInd]
            newSecLen = inidiff / (howMany[secInd] + 1)
            heapq.heappush(pq, (newSecLen*(-1), secInd))

        return pq[0][0]*(-1)
    
    # Most Optimal Solution usig BS on ans
    def minimiseMaxDistance_OP(arr, k: int) -> float:
        def numberOfGasStationsRequired(dist, arr):
            n = len(arr)  # size of the array
            cnt = 0
            for i in range(1, n):
                segment_length = arr[i] - arr[i - 1]
                numberInBetween = segment_length // dist  # Use integer division

                # Adjust for perfect divisibility
                if segment_length % dist == 0:
                    numberInBetween -= 1
                
                cnt += numberInBetween
            return cnt 

        n = len(arr)  # size of the array
        low = 0
        high = 0

        # Find the maximum distance:
        for i in range(n - 1):
            high = max(high, arr[i + 1] - arr[i])
        ans = high  # Initialize ans to the maximum possible value

        # Apply Binary search:
        diff = 1e-6
        while high - low > diff:
            mid = (low + high) / 2.0
            cnt = numberOfGasStationsRequired(mid, arr)
            if cnt > k:
                low = mid
            else:
                ans = mid
                high = mid
        return high # or ans

arr = [1,2,3,4,5,6,7]
k = 6
print(Solution.minimiseMaxDistance_BF(arr,k))
print(Solution.minimiseMaxDistance_BT(arr,k))
print(Solution.minimiseMaxDistance_OP(arr,k))
