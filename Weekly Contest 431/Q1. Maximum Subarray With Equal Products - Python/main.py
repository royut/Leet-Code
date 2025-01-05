def lcmCalc(multiples):
    lcm = 1
    for multiple in multiples:
        temp = 1
        for num in multiple:
            temp = temp * num
            if lcm % temp != 0:
                lcm *= num
    return lcm


def gcdCalc(nums, min):
    gcd = 1
    flag = True
    for i in range(min, 0, -1):
        for num in nums:
            if num % i != 0:
                flag = False
        if flag == True:
            gcd = i
            break
    return gcd


class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum = min(nums)
        maxNum = max(nums)
        primes = [2, 3, 5, 7]
        multiples = []
        for num in nums:
            numMultiples = []
            for prime in primes:
                while num % prime == 0:
                    numMultiples.append(prime)
                    num = num // prime
            multiples.append(numMultiples)
        lcm = lcmCalc(multiples)
        gcd = gcdCalc(nums, minNum)
        prod = 1
        for num in nums:
            prod *= num
        print(nums, lcm, gcd, prod)
        while prod > lcm * gcd:
            i = nums.index(maxNum)
            nums.pop(i)
            prod = prod // maxNum
            maxNum = max(nums)
            minNum = min(nums)
            multiples.pop(i)
            lcm = lcmCalc(multiples)
            gcd = gcdCalc(nums, minNum)
        print(nums)
        return len(nums)


if __name__ == '__main__':
    print('in main')
    nums = [1, 2, 3, 1, 4, 5, 1]
    nums = [1, 2, 1, 1, 1]
    nums = [2,4,6]
    nums = [1,2,1,2,1,1,1]
    print(Solution().maxLength(nums))
