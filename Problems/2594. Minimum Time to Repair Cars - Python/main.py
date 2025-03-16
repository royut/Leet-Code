from math import sqrt


class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        right = min(ranks) * cars * cars
        left = 1
        while left <= right:
            mid = (left + right) // 2
            if self.checkTime(ranks, cars, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def checkTime(self, ranks, cars, time):
        carAmount = 0
        for i in range(len(ranks)):
            carAmount += int(sqrt(time / ranks[i]))
        return carAmount >= cars


if __name__ == '__main__':
    print('in main')
    ranks = [5,1,8]
    cars = 6
    print(Solution().repairCars(ranks, cars))