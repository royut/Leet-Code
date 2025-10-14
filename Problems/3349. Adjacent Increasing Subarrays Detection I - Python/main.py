class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        order = [0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                order.append(1)
            else:
                order.append(0)
        # print(order)
        required1 = [1] * (2 * k)
        required2 = [0] + [1] * (2 * (k-1)) + [1]
        required3 = ([0] + [1] * (k-1)) * 2
        required4 = ([1] * k) + [0] + ([1] * (k-1))
        # print(required1, required2, required3, required4)
        for i in range(len(order) - 2 * k + 1):
            # print(order[i:i+2*k])
            if order[i:i+2*k] in [required1, required2, required3, required4]:
                return True
        return False


if __name__ == "__main__":
    print('in main')
    nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
    k = 3
    print(Solution().hasIncreasingSubarrays(nums, k))