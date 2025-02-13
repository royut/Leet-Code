class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return len(set(nums))
        nums = sorted(nums)
        if k > len(nums):
            fn = []
            ln = []
            added = 0
            subbed = 0
            for i in range(len(nums)):
                print(i)
                if i == 0:
                    fn.append(nums[0] - k)
                    added += 1
                    ln.append(nums[-1] + k)
                    subbed += 1
                else:
                    if (fn[0] + added <= nums[i] + k) and (fn[0] + added >= nums[i] - k):
                        print('if 1')
                        fn.append(fn[0] + added)
                        added += 1
                    else:
                        print('if 2')
                        fn.append(nums[i])
                    if (ln[-1] - subbed <= nums[i] + k) and (ln[-1] - subbed >= nums[i] - k):
                        ln.insert(0, ln[-1] - subbed)
                        subbed += 1
                    else:
                        ln.insert(0, nums[i])

            print(fn)
            print(ln)
            return max(len(set(fn)), len(set(ln)))
        else:
            f = []
            flag = 0
            for i in range(len(nums)):
                flag = 0
                for j in range(-k, k + 1):
                    if nums[i] + j not in f:
                        f.append(nums[i] + j)
                        flag = 1
                        break
                if flag == 0:
                    f.append(nums[i])
            print(f)
            return len(set(f))


if __name__ == '__main__':
    print('in main')
    nums = [7,9,10,7,7,9,8,5,10,8]
    print(Solution().maxDistinctElements(nums, 2))
