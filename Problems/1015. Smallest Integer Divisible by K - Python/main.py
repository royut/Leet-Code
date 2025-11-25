class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        mods = set()
        curr = 1
        currLen = 1
        while True:
            if curr % k == 0:
                return currLen
            else:
                if curr % k in mods:
                    return -1
                mods.add(curr % k)
            curr = curr * 10 + 1
            currLen += 1


if __name__ == '__main__':
    k = 1
    print(Solution().smallestRepunitDivByK(k))