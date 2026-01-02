def aggressiveCows(stalls, k):
    """
    Function to determine the maximum possible minimum distance between k cows placed in stalls.
    
    Args:
    stalls (list): List of integers representing stall positions.
    k (int): Number of cows to place.

    Returns:
    int: Maximum possible minimum distance.
    """
    def canPlace(stalls, distance, k):
        """
        Helper function to check if we can place k cows with at least 'distance' between them.
        
        Args:
        stalls (list): Sorted list of stall positions.
        distance (int): Minimum distance to check.
        k (int): Number of cows to place.

        Returns:
        bool: True if placement is possible, False otherwise.
        """
        count_cows = 1  # Place the first cow in the first stall
        last_position = stalls[0]

        for i in range(1, len(stalls)):
            # Place the next cow if the distance between current stall and last cow's position is >= distance
            if (stalls[i] - last_position) >= distance:
                count_cows += 1
                last_position = stalls[i]  # Update the last placed cow's position
            # If all cows are placed, return True
            if count_cows >= k:
                return True

        return False

    # Sort the stall positions
    stalls.sort()
    max_distance = stalls[-1] - stalls[0]  # Maximum possible distance

    # Check every possible distance from 1 to max_distance
    for distance in range(1, max_distance + 1):
        # If the current distance is not feasible, return the previous feasible distance
        if not canPlace(stalls, distance, k):
            return distance - 1

    return max_distance  # If all distances are feasible


def aggressiveCows(stalls, k):
    def canPlace(stalls, distance, k):
        count_cows = 1  # Place the first cow
        last_position = stalls[0]

        for i in range(1, len(stalls)):
            if (stalls[i] - last_position) >= distance:
                count_cows += 1
                last_position = stalls[i]
            if count_cows >= k:
                return True

        return False

    stalls.sort()

    # Binary search on the distance range
    low, high = 1, stalls[-1] - stalls[0]
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if canPlace(stalls, mid, k):
            ans = mid  # Try for a larger distance
            low = mid + 1
        else:
            high = mid - 1

    return ans

stalls = [0, 3, 4, 7, 10, 9]
cows = 4
print(aggressiveCows(stalls,cows))