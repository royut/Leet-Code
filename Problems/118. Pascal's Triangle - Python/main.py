class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]
        if numRows == 1:
            return ans
        for i in range(1, numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(ans[i-1][j-1] + ans[i-1][j])
            # print(temp)
            ans.append(temp)
        return ans


if __name__ == "__main__":
    n = 5
    print(Solution().generate(n))