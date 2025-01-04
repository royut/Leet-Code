class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        commonPrefix = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(strs[i]), -1, -1):
                if strs[i][:j] == commonPrefix[:j]:
                    commonPrefix = commonPrefix[:j]
                    break
            if commonPrefix == "":
                break
        return commonPrefix


if __name__ == '__main__':
    print('in main')
    words = ['flower', 'flow', 'flight']
    print(Solution().longestCommonPrefix(words))
