class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        def findInPotions(spell):
            low, high = 0, len(potions) - 1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if potions[mid] * spell >= success:
                    idx = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return idx

        potions.sort()
        spellsSuccess = []
        lenPotions = len(potions)
        for spell in spells:
            successRate = findInPotions(spell)
            if successRate != -1:
                spellsSuccess.append(lenPotions - successRate)
            else:
                spellsSuccess.append(0)
        return spellsSuccess


if __name__ == '__main__':
    print('in main')
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    print(Solution().successfulPairs(spells, potions, success))