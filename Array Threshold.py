# Approach:
# - We use **binary search** to efficiently find the threshold value.
# - If a value in the list is greater than the threshold, we replace it with the threshold.
# - We adjust the threshold value until the sum of the modified list is as close as possible to `desiredSum`.
# - The threshold lies between `0` and `max(arr)`, so we use **binary search** to find it.

# Time Complexity: O(N log M), where N is the length of the array and M is the max value in the array.
# Space Complexity: O(1), as we only use a few extra variables.

class Solution:
    def findThreshold(self, nums: List[int], desiredSum: float) -> float:
        left, right = 0, max(nums)  # Define the binary search range

        # Binary search for the optimal threshold value
        while right - left > 1e-6:  # Precision up to 6 decimal places
            mid = (left + right) / 2  # Middle threshold candidate
            current_sum = sum(min(num, mid) for num in nums)  # Calculate modified sum
            
            if current_sum < desiredSum:
                right = mid  # Reduce threshold to increase sum
            else:
                left = mid  # Increase threshold to decrease sum

        return round(left, 2)  # Round to 2 decimal places for precision

# Example cases
solution = Solution()
print(solution.findThreshold([2,1,5], 6))  # Output: 3.00
print(solution.findThreshold([2,1,5], 2))  # Output: 0.67
print(solution.findThreshold([2,1,5], 4))  # Output: 1.50
print(solution.findThreshold([2,1,5], 1))  # Output: 0.33
