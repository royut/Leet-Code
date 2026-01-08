class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        dp = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(float('-inf'))
            dp.append(temp)
        dp[-1][-1] = nums1[-1] * nums2[-1]
        for i in range(n-2, -1, -1):
            dp[-1][i] = max(dp[-1][i+1], nums1[i] * nums2[-1])
        for j in range(m-2, -1, -1):
            dp[j][-1] = max(dp[j+1][-1], nums1[-1] * nums2[j])
        # print(dp)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = max(
                    dp[i+1][j],
                    dp[i][j+1],
                    dp[i+1][j+1] + (nums1[j] * nums2[i]),
                    nums1[j] * nums2[i],
                )
        # print(dp)
        return dp[0][0]


if __name__ == "__main__":
    print('in main')
    nums1 = [2, 1, -2, 5]
    nums2 = [3, 0, -6]
    nums1 = [3, -2]
    nums2 = [2, -6, 7]
    nums1 = [-1, -1]
    nums2 = [1, 1]
    nums1 = [-5, -1, -2]
    nums2 = [3, 3, 5, 5]
    nums1 = [5, -4, -3]
    nums2 = [-4, -3, 0, -4, 2]
    print(Solution().maxDotProduct(nums1, nums2))