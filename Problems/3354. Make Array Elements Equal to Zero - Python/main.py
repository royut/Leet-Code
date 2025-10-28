class Solution(object):
    def isValidSelection(self, nums, pos, direction, count):
        # print(nums, pos, direction, count)
        while 0 <= pos <= len(nums) - 1:
            # print(pos, nums, direction, count)
            if nums[pos] == 0:
                pos += direction
            else:
                nums[pos] -= 1
                direction *= -1
                pos += direction
                count -= 1
            if count == 0:
                return True
        return False

    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positions = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                positions.append(i)
            count += nums[i]
        valiPositions = 0
        for pos in positions:
            direction = -1  # -1: left, 1: right
            tempNums = nums[:]
            valiPositions += self.isValidSelection(tempNums, pos, direction, count)
            direction = 1
            tempNums = nums[:]
            valiPositions += self.isValidSelection(tempNums, pos, direction, count)
        return valiPositions


if __name__ == "__main__":
    print('in main')
    nums = [1, 0, 2, 0, 3]
    print(Solution().countValidSelections(nums))