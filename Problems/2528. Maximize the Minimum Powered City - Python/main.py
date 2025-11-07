class Solution(object):
    def checkMin(self, stations, r, k, minPower, cnt):
        diff = cnt[:]
        total = 0
        for i in range(len(stations)):
            total += diff[i]
            if total < minPower:
                add = minPower - total
                if k < add:
                    return False
                k -= add
                end = min(len(stations), i + 2 * r + 1)
                diff[end] -= add
                total += add
        return True

    def maxPower(self, stations, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        n = len(stations)
        cnt = [0] * (n + 1)
        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            cnt[left] += stations[i]
            cnt[right] -= stations[i]

        print(self.checkMin(stations, r, k, 6, cnt))
        high, low = sum(stations) + k, min(stations)
        res = 0
        while low <= high:
            mid = (high + low) // 2
            if self.checkMin(stations, r, k, mid, cnt):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res


if __name__ == '__main__':
    print('in main')
    stations = [1, 2, 4, 5, 0]
    r = 1
    k = 2
    print(Solution().maxPower(stations, r, k))