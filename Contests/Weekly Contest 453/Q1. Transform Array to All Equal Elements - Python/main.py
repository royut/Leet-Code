class Solution(object):
    def canMakeEqual(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        np = 0
        numsp = []
        countp = 0
        nn = 0
        numsn = []
        countn = 0
        for i in range(n):
            numsp.append(nums[i])
            numsn.append(nums[i])
        for num in nums:
            if num == 1:
                np += 1
            else:
                nn += 1
        if nn % 2 == 0:
            for i in range(n-1):
                if numsp[i] == -1:
                    numsp[i] *= -1
                    numsp[i+1] *= -1
                    countp += 1
            if numsp[-1] != 1:
                countp = k+1
        else:
            countp = k+1
        if np % 2 == 0:
            for i in range(n-1):
                if numsn[i] == 1:
                    numsn[i] *= -1
                    numsn[i+1] *= -1
                    countn += 1
            if numsn[-1] != -1:
                countn = k+1
        else:
            countn = k+1
        return min(countn, countp) <= k


if __name__ == '__main__':
    print('in main')
    nums = [1, -1, 1, -1, 1]
    k = 3
    # nums = [-1,-1,-1,1,1,1]
    # k = 5
    print(Solution().canMakeEqual(nums, k))
