class Solution(object):
    def makeRevese(self, num):
        newNum = 0
        while num > 0:
            d = num % 10
            num //= 10
            newNum = newNum * 10 + d
        return newNum

    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        poses = {}
        for i in range(len(nums)):
            if nums[i] not in poses:
                poses[nums[i]] = [i]
            else:
                poses[nums[i]].append(i)
        # print(poses)
        minPair = float("inf")
        for i in range(len(poses)):
            temp = self.makeRevese(nums[i])
            if temp in poses:
                # print(temp, i, poses[temp])
                for j in poses[temp]:
                    if j > i:
                        minPair = min(minPair, abs(i - j))
                        break
        if minPair == float("inf"):
            return -1
        return minPair


if __name__ == '__main__':
    print('in main')
    nums = [12, 21, 45, 33, 54]
    nums = [21, 120]
    print(Solution().minMirrorPairDistance(nums))