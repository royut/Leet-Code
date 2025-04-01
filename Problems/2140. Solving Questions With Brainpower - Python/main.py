class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        res = [0] * n
        res[-1] = questions[-1][0]
        for i in range(n-2, -1, -1):
            solve = questions[i][0]
            if i + questions[i][1] + 1 < n:
                solve += res[i + questions[i][1] + 1]
            res[i] = max(solve, res[i+1])
        return res[0]


if __name__ == '__main__':
    print('in main')
    questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    print(Solution().mostPoints(questions))