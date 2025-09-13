class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = "aeiou"
        vs = {}
        cs = {}
        for char in s:
            if char in vowels:
                if char not in vs:
                    vs[char] = 1
                else:
                    vs[char] += 1
            else:
                if char not in cs:
                    cs[char] = 1
                else:
                    cs[char] += 1
        maxV = 0
        maxS = 0
        for v in vs:
            # print(vs[v])
            maxV = max(maxV, vs[v])
        for c in cs:
            # print(cs[c])
            maxS = max(maxS, cs[c])
        return maxV + maxS


if __name__ == '__main__':
    print('in main')
    s = "successes"
    s = "aeiaeia"
    print(Solution().maxFreqSum(s))