class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sumArr = []
        currSum = 0
        for i in range(len(arr)):
            currSum += arr[i]
            sumArr.append(currSum)
        print('aa', sumArr)
        print('aa', arr)
        oddSumArray = 0
        evenToHere = 0
        for i in range(len(arr)):
            if sumArr[i] % 2 == 1:
                oddSumArray += 1 + evenToHere
                evenToHere = 0
            if sumArr[i] % 2 == 0:
                evenToHere += 1
                oddSumArray += 1
        print(oddSumArray)


if __name__ == '__main__':
    print('in main')
    # arr = [1, 3, 5]
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(Solution().numOfSubarrays(arr))
