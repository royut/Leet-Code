class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        cells = maxWeight // w
        if cells >= n * n:
            return n * n
        else:
            return cells


if __name__ == '__main__':
    print('in main')
    print(Solution().maxContainers(3,5,20))