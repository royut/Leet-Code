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
        ans = {}
        ansList = []
        for q in queries:
            if q not in ans:
                numToFind = nums[q]
                # print('to fiund', numToFind, q)
                if numToFind not in locs or len(locs[numToFind]) == 1:
                    ans[q] = (-1)
                else:
                    qIndex = locs[numToFind].index(q)
                    before = locs[numToFind][qIndex-1]
                    if qIndex == len(locs[numToFind])-1:
                        after = locs[numToFind][0]
                    else:
                        after = locs[numToFind][qIndex+1]
                    # print(locs[numToFind], q, qIndex, before, after)
                    distBefore = min(abs(before - q), abs(len(nums) - abs(before - q)))
                    distAfter = min(abs(after - q), abs(len(nums) - abs(after - q)))
                    minDist = min(distBefore, distAfter)
                    ans[q] = minDist
                ansList.append(ans[q])
            else:
                ansList.append(ans[q])
                # print('ans', ans)
        return ansList


if __name__ == '__main__':
    print('in main')
    nums = [5,20,12,14,12,17,13,7,7,5,20,5,5,5,12,19,6]
    queries = [3,14,2,0,8,12,16,6,7,11,4,10]
    print(Solution().solveQueries(nums, queries))