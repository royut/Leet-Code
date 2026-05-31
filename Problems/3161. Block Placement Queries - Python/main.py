from sortedcontainers import SortedList


class Solution(object):
    def __init__(self):
        self.max = 65536
        self.walls = SortedList()
        self.d = []

    def update(self, value):
        # print(self.d, self.walls)
        index = self.walls.bisect_left(value)
        prv = self.walls[index-1]
        nxt = self.walls[index]
        # print(prv, nxt, value)
        self.walls.add(value)
        self.d[self.max + value] = value - prv
        self.updateLookUp(value)
        self.d[self.max + nxt] = nxt - value
        self.updateLookUp(nxt)
        # print(self.d[65535:65535+20], self.walls)
        # print(self.d[32768:32768+20])

    def updateLookUp(self, i):
        i += self.max
        while i > 1:
            i >>= 1
            self.d[i] = max(self.d[2*i], self.d[2*i+1])

    def query(self, value):
        print(self.d[self.max:self.max+64])
        print(self.d[self.max//2:self.max//2+32])
        print(self.d[self.max//4:self.max//4+16])
        print(self.d[self.max//8:self.max//8+8])
        print(self.d[self.max//16:self.max//16+4])
        print(self.d[self.max//32:self.max//32+2])
        print(self.d[self.max//64:self.max//64+1])
        index = self.walls.bisect_right(value)
        prv = self.walls[index-1]
        lastSeg = value - prv
        print("query", value, prv, self.walls[index-1], self.walls, lastSeg)
        print(self.d[self.max:self.max+prv+1])
        r = prv + self.max
        l = self.max
        treeMax = 0
        # print("prevs", prv, treeMax)
        i = self.max
        print("slr", l-i, r-i, treeMax, self.d[l], self.d[r], self.d[l:r+1])
        while l < r:
            treeMax = max(treeMax, self.d[l], self.d[r])
            if not r & 1:
                # treeMax = max(treeMax, self.d[l], self.d[r])
                r -= 1
            l >>= 1
            r >>= 1
            treeMax = max(treeMax, self.d[l], self.d[r])
            i //= 2
            print("lr", l-i, r-i, treeMax, self.d[l], self.d[r], self.d[l:r+1])
        print("\nmaxees", treeMax, lastSeg)
        return max(lastSeg, treeMax)

    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        self.walls = SortedList([0, self.max-1])
        self.d = [0] * (self.max * 2)
        ans = []
        for q in queries:
            if q[0] == 1:
                self.update(q[1])
            if q[0] == 2:
                ans.append(self.query(q[1]) >= q[2])
        # print(self.walls)
        # print(self.d[65535::100])
        return ans


if __name__ == "__main__":
    print('in main')
    # queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]
    # queries = [[1, 7], [2, 6, 6], [1, 2], [2, 6, 5], [2, 8, 6]]
    # queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]
    # queries = [[1, 1], [2, 2, 3]]
    # queries = [[1, 3], [2, 4, 2]]
    queries = [[1, 7], [1, 6], [2, 4, 9], [1, 11], [2, 11, 5]]
    # queries = [[1, 118], [1, 29], [1, 101], [1, 84], [1, 10], [1, 33], [1, 40], [1, 148], [1, 113], [1, 67], [1, 121], [1, 8], [1, 81], [1, 133], [1, 100], [1, 108], [1, 20], [1, 7], [1, 56], [1, 16], [1, 6], [1, 123], [1, 72], [1, 34], [1, 87], [1, 61], [2, 51, 16], [1, 83], [1, 143]]
    # queries = [[1, 56], [1, 145], [1, 110], [1, 108], [1, 114], [1, 61], [1, 144], [1, 79], [1, 46], [1, 129], [1, 134], [1, 138], [1, 148], [1, 146], [2, 115, 45]]
    print(Solution().getResults(queries))