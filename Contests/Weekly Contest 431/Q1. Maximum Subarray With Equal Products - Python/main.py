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
    for i in range(min, 0, -1):
        flag = True
        for num in nums:
            if num % i != 0:
                flag = False
        if flag == True:
            gcd = i
            break
    return gcd


def prodCalc(nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod


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
        prod = prodCalc(nums)
        maxLength = 0
        for i in range(len(nums) + 1):
            for j in range(i + 1, len(nums) + 1):
                # print(nums[i:j])
                if prodCalc(nums[i:j]) == gcdCalc(nums[i:j], min(nums[i:j])) * lcmCalc(multiples[i:j]):
                    # print(i,j, nums[i:j], prodCalc(nums[i:j]), gcdCalc(nums[i:j], min(nums[i:j])), lcmCalc(multiples[i:j]), j - i + 1)
                    if maxLength < j - i:
                        maxLength = j - i
        return maxLength


if __name__ == '__main__':
    print('in main')
    nums = [1, 2, 3, 1, 4, 5, 1]
    nums = [1, 2, 1, 1, 1]
    nums = [2,4,6]
    nums = [1,2,1,2,1,1,1]
    # nums = [2,3,4,5,6]
    nums = [4,6]
    print(Solution().maxLength(nums))
