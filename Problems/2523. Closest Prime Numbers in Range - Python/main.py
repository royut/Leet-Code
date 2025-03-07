class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        primes = [True for i in range(right+1)]
        current = 2
        while current * current <= right:
            if primes[current]:
                for i in range(current*current, right+1, current):
                    primes[i] = False
            current += 1
        primes[1] = False
        min1, min2 = -1, -1
        lastIndex = -1
        for i in range(left, right+1):
            if primes[i]:
                if min1 == -1:
                    min1 = i
                elif min2 == -1:
                    min2 = i
                elif i - lastIndex < min2 - min1:
                    min1 = lastIndex
                    min2 = i
                lastIndex = i
        if min1 == -1 or min2 == -1:
            return [-1, -1]
        return [min1, min2]


if __name__ == '__main__':
    print('in main')
    left = 1
    right = 1000000
    print(Solution().closestPrimes(left, right))