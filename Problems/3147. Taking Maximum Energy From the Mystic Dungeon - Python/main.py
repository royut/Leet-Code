class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)
        maxEnergy = float('-inf')
        for i in range(n-k, n):
            # print('i', i)
            j = i
            total = 0
            while j >= 0:
                total += energy[j]
                j -= k
                # print(total)
                maxEnergy = max(maxEnergy, total)
        return maxEnergy


if __name__ == "__main__":
    print("in main")
    energy = [5, 2, -10, -5, 1]
    k = 3
    energy = [-2, -3, -1]
    k = 2
    print(Solution().maximumEnergy(energy, k))