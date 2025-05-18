class Solution(object):
    def sumOfDigits(self, n):
        s = 0
        while n > 0:
            s += n % 10
            n = n // 10
        return s

    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i = 0
        j = 0
        k = l
        swaps = 0

        while i < n1 and j < n2:
            if self.sumOfDigits(L[i]) < self.sumOfDigits(R[j]):
                arr[k] = L[i]
                i += 1
            elif self.sumOfDigits(L[i]) > self.sumOfDigits(R[j]):
                arr[k] = R[j]
                j += 1
                swaps += 1
            else:
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                    swaps += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

        return swaps

    def mergeSort(self, arr, l, r):
        if l < r:
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l + (r - l) // 2

            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            print(self.merge(arr, l, m, r))

    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = list(nums)
        self.mergeSort(sorted_nums, 0, len(sorted_nums) - 1)
        print(nums)
        print(sorted_nums)
        countDiffs = 0
        for i in range(0, len(sorted_nums)):
            if nums[i] != sorted_nums[i]:
                countDiffs += 1
        if countDiffs % 2 == 0:
            return countDiffs // 2
        else:
            return countDiffs // 2 + 1


if __name__ == '__main__':
    print('in main')
    nums = [37, 100]
    # nums = [22, 14, 33, 7]
    nums = [18, 43, 34, 16]
    # nums = [277993448,416038674,616955867,539372283]
    print(Solution().minSwaps(nums))
