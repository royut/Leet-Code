class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        table = []
        for i in range(len(mana)):
            temp = [mana[i]*skill[0]]
            for j in range(1, len(skill)):
                temp.append(temp[-1] + mana[i]*skill[j])
            table.append(temp)
            # print(temp)
            if i > 0:
                maxTimeDiff = min(table[i-1])
                for j in range(len(skill)-1):
                    if table[i-1][j+1] - table[i][j] > maxTimeDiff:
                        maxTimeDiff = table[i-1][j+1] - table[i][j]
                for j in range(len(skill)):
                    table[i][j] += maxTimeDiff
                # print(maxTimeDiff)
        # print(table)
        return table[-1][-1]