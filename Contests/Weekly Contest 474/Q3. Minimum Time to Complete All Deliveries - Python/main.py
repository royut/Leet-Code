class Solution(object):
    def minimumTime(self, d, r):
        """
        :type d: List[int]
        :type r: List[int]
        :rtype: int
        """
        dc = d[:]
        hour = 1
        while d[0] > 0 or d[1] > 0:
            f0 = hour % r[0] != 0
            f1 = hour % r[1] != 0
            # print(hour, f0, f1)
            if f0 and not f1:
                d[0] -= 1
            elif f1 and not f0:
                d[1] -= 1
            elif f0 and f1:
                if d[0] <= 0:
                    d[1] -= 1
                elif d[1] <= 0:
                    d[0] -= 1
                else:
                    d[0] -= 1
            hour += 1
            # print(d)
        hourc = 1
        while dc[0] > 0 or dc[1] > 0:
            f0 = hourc % r[0] != 0
            f1 = hourc % r[1] != 0
            # print(hour, f0, f1)
            if f0 and not f1:
                dc[0] -= 1
            elif f1 and not f0:
                dc[1] -= 1
            elif f0 and f1:
                if dc[0] <= 0:
                    dc[1] -= 1
                elif dc[1] <= 0:
                    dc[0] -= 1
                else:
                    dc[1] -= 1
            hourc += 1
            # print(dc)
        print(hour, hourc)
        return min(hour, hourc) - 1


if __name__ == '__main__':
    print('in main')
    d = [3, 1]
    r = [2, 3]
    # d = [1, 3]
    # r = [2, 2]
    # d = [2, 1]
    # r = [3, 4]
    # d = [1, 4]
    # r = [3, 5]
    d = [2, 2]
    r = [3, 4]
    print(Solution().minimumTime(d, r))
