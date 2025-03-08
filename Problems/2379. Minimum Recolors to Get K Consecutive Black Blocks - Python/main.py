class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        minChanges = float('inf')
        for i in range(0, len(blocks)-k+1):
            tempChanges = blocks[i:i+k].count('W')
            if tempChanges < minChanges:
                minChanges = tempChanges
            # print(i, i+k, blocks[i:i+k], tempChanges)
        return minChanges


if __name__ == '__main__':
    print('in main')
    blocks = "WBBWWBBWBW"
    k = 7
    blocks = "WBWBBBW"
    k = 2
    print(Solution().minimumRecolors(blocks, k))
