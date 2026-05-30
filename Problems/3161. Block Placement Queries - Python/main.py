class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        d = [0, float('inf')]
        ans = []
        for q in queries:
            if q[0] == 1:
                i = 0
                for i in range(len(d)):
                    if d[i] > q[1]:
                        break
                d.insert(i, q[1])
                # print(i, d)
            if q[0] == 2:
                prev = 0
                # print(q)
                for i in range(1, len(d)):
                    curr = d[i]
                    if d[i] > q[1]:
                        curr = q[1]
                    # print(prev, curr)
                    if curr - prev >= q[2]:
                        ans.append(True)
                        break
                    if d[i] > q[1]:
                        ans.append(False)
                        break
                    prev = curr
        # print(ans)
        return ans


if __name__ == "__main__":
    print('in main')
    queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]
    # queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]
    print(Solution().getResults(queries))