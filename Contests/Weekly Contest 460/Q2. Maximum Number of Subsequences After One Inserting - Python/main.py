class Solution(object):
    def numOfSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        index = 0
        while index < len(s):
            if s[index] not in ['L', 'C', 'T']:
                s.pop(index)
            else:
                index += 1
        if 'T' not in s:
            s.insert(len(s), 'T')
        elif 'C' not in s:
            tindex = s.index('T')
            s.insert(tindex, 'C')
        else:
            s.insert(len(s), 'T')
        print(s)
        Ts = [0 for _ in range(len(s))]
        temp = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'T':
                temp += 1
            Ts[i] = temp
        print(Ts)
        Cs = [0 for _ in range(len(s))]
        temp = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'C':
                Cs[i] = Ts[i]
                temp += Cs[i]
            Cs[i] = temp
        print(Cs)
        Ls = [0 for _ in range(len(s))]
        temp = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'L':
                Ls[i] = Cs[i]
                temp += Ls[i]
            Ls[i] = temp
        print(Ls)
        return Ls[0]


if __name__ == '__main__':
    print('in main')
    # s = "LMCT"
    s = "LCCT"
    s = "LT"
    s = "LCTKLCLT"
    # s = "TTGCLCEL"
    print(Solution().numOfSubsequences(s))