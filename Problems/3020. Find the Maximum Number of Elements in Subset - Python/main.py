class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictNums = {}
        nums.sort()
        for num in nums:
            if num not in dictNums:
                dictNums[num] = 1
            else:
                dictNums[num] += 1
        # print(dictNums)
        maxLength = 0
        for num in dictNums:
            tempLength = 0
            if num == 1:
                if dictNums[1] % 2 == 0:
                    tempLength = dictNums[1] - 1
                else:
                    tempLength = dictNums[1]
            else:
                index = 1
                curr = num
                while True:
                    # print(curr, dictNums[curr], curr*curr in dictNums)
                    if dictNums[curr] >= 2 and curr * curr in dictNums:
                        curr = curr * curr
                        index += 1
                    else:
                        break
                tempLength = index * 2 - 1
            if tempLength > maxLength:
                maxLength = tempLength
        return maxLength


if __name__ == "__main__":
    print('in main')
    nums = [5, 4, 1, 2, 2]
    nums = [1, 3, 2, 4]
    print(Solution().maximumLength(nums))