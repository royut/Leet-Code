class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        countDistance = 0
        for i in range(len(arr1)):
            distanceFlag = False
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    distanceFlag = True
                    break
            if not distanceFlag:
                countDistance += 1
        return countDistance


if __name__ == "__main__":
    print('in main')
    arr1 = [4, 5, 8]
    arr2 = [10, 9, 1, 8]
    d = 2
    print(Solution().findTheDistanceValue(arr1, arr2, d))