class Solution(object):
    def minArraySum(self, nums, k, op1, op2):
        """
        :type nums: List[int]
        :type k: int
        :type op1: int
        :type op2: int
        :rtype: int
        """
        while op1 > 0 or op2 > 0:
            op1s = []
            op2s = []
            max_op1 = 0
            max_op2 = 0
            op1_i = 0
            op2_i = 0

            for i in range(len(nums)):

                op1_n = int(round(nums[i] / 2))
                if op1 > 0:
                    if op1_n > max_op1:
                        max_op1 = op1_n
                        op1_i = i

                if nums[i] >= k:
                    op2_n = k
                else:
                    op2_n = 0

                if op2 > 0:
                    if op2_n > max_op2:
                        max_op2 = op2_n
                        op2_i = i
                    if op2_n == max_op2:
                        if nums[i] % 2 == 1 and nums[op2_i] % 2 == 0:
                            max_op2 = op2_n
                            op2_i = i

            # print(max_op1, max_op2)

            if max_op1 > max_op2 and op1 > 0:
                # print("1")
                nums[op1_i] = int(round(nums[op1_i] / 2))
                op1 -= 1

            if max_op2 > max_op1 and op2 > 0:
                # print("2")
                nums[op2_i] = nums[op2_i] - k
                op2 -= 1

            print(nums)
        return sum(nums)


if __name__ == '__main__':
    print("in main")
    print(Solution().minArraySum([2,8,3,19,3], 3, 1, 1))
