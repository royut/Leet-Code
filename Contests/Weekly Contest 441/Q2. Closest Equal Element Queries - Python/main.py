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
            # print('to fiund', numToFind, q)
            if numToFind not in locs or len(locs[numToFind]) == 1:
                ans.append(-1)
            else:
                # print(locs[numToFind],q)
                minDist = float('inf')
                for numFound in locs[numToFind]:
                    # print(numFound - q)
                    dist = min(abs(numFound - q), abs(len(nums) - abs(numFound - q)))
                    if dist < minDist and dist != 0:
                        minDist = dist
                ans.append(minDist)
            # print('ans', ans)
        return ans


if __name__ == '__main__':
    print('in main')
    nums = [1,3,1,4,1,3,2]
    queries = [0,3,5]
    print(Solution().solveQueries(nums, queries))