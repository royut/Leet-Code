class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        candies = sorted(candies)
        left, right = 1, candies[-1]
        if not self.canGetCandies(candies, k, left):
            return 0
        while left <= right:
            mid = (left + right) // 2
            if self.canGetCandies(candies, k, mid):
                left = mid + 1
            else:
                right = mid - 1
        return right

    def canGetCandies(self, candies, k, c):
        i = len(candies) - 1
        while True:
            curr = candies[i]
            kids = curr // c
            k -= kids
            if k <= 0:
                return True
            elif i == 0:
                return False
            i -= 1


if __name__ == '__main__':
    print('in main')
    candies = [4,7,5]
    k = 4
    candies = [1,2,3,4,10]
    k = 5
    print(Solution().maximumCandies(candies, k))
