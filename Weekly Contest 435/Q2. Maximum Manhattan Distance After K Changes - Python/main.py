class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        string = s
        changes = k
        i, j = 0, 0
        ii, jj = 0, 0
        n, s, e, w = 0, 0, 0, 0
        maxdis = 0
        for d in string:
            k = changes
            if d == 'N':
                ii += 1
                n += 1
            elif d == 'S':
                ii -= 1
                s += 1
            elif d == 'E':
                jj += 1
                e += 1
            elif d == 'W':
                jj -= 1
                w += 1
            # check
            i = ii
            j = jj
            if i > 0:
                if s > k:
                    i += 2*k
                    k = 0
                else:
                    i += 2*s
                    k = k - s
            elif i < 0:
                if n > k:
                    i -= 2*k
                    k = 0
                else:
                    i -= 2*n
                    k = k - n
            elif i == 0:
                if n > k:
                    i += 2*k
                    k = 0
                else:
                    i += 2*n
                    k = k - n
            if j > 0:
                if w > k:
                    j += 2*k
                    k = 0
                else:
                    j += 2*w
                    k = k - w
            elif j < 0:
                if e > k:
                    j -= 2*k
                    k = 0
                else:
                    j -= 2*e
                    k = k - e
            elif j == 0:
                if w > k:
                    j += 2*k
                    k = 0
                else:
                    j += 2*w
                    k = k - w
            if abs(i) + abs(j) > maxdis:
                maxdis = abs(i) + abs(j)
            # print(maxdis,ii,jj, i, j)
        return maxdis


if __name__ == '__main__':
    print('in main')
    print(Solution().maxDistance('NWSE', 1))