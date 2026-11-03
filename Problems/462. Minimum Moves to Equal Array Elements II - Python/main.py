class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = int(self.find_median(nums))
        moves1 = 0
        moves2 = 0
        for num in nums:
            moves1 += abs(num - median)
            moves2 += abs(num - (median+1))
        return min(moves1, moves2)

    def find_median(self, numbers):
        if not numbers:
            return None

        # 1. Sort the list in ascending order
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        mid = n // 2

        # 2. Check if the total count is even or odd
        if n % 2 == 0:
            # Even: average of the two middle elements
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        else:
            # Odd: the exact middle element
            return sorted_nums[mid]


if __name__ == "__main__":
    print('in main')
    nums = [1, 2, 3]
    nums = [1, 10, 2, 9]
    print(Solution().minMoves2(nums))