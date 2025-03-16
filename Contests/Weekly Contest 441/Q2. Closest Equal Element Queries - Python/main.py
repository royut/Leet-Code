class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        locs = {}
        for i in range(len(nums)):
            if nums[i] not in locs:
                locs[nums[i]] = [i]
            else:
                locs[nums[i]].append(i)
        # print(locs)
        ans = []
        for q in queries:
            numToFind = nums[q]
            rightIndex = q+1
            leftIndex = q-1
            if rightIndex >= len(nums):
                rightIndex -= len(nums)
            if leftIndex < 0:
                leftIndex += len(nums)
            foundFlag = False
            # print('q', q, numToFind)
            while True:
                # print('indexes', leftIndex, rightIndex)
                if numToFind == nums[leftIndex] and leftIndex != q:
                    dist = min(abs(q - leftIndex), abs(len(nums) - abs(q - leftIndex)))
                    ans.append(dist)
                    foundFlag = True
                    break
                if numToFind == nums[rightIndex] and rightIndex != q:
                    dist = min(abs(rightIndex - q), abs(len(nums) - abs(q - rightIndex)))
                    ans.append(dist)
                    foundFlag = True
                    break
                if rightIndex == leftIndex:
                    break
                rightIndex += 1
                leftIndex -= 1
                if rightIndex >= len(nums):
                    rightIndex -= len(nums)
                if leftIndex < 0:
                    leftIndex += len(nums)
            # print(foundFlag)
            if not foundFlag:
                ans.append(-1)
            # print(ans)
        return ans


if __name__ == '__main__':
    print('in main')
    nums = [5,20,12,14,12,17,13,7,7,5,20,5,5,5,12,19,6]
    queries = [3,14,2,0,8,12,16,6,7,11,4,10]
    print(Solution().solveQueries(nums, queries))