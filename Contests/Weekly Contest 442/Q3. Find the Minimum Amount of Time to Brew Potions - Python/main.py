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
            if i > 0:
                if len(skill) >= 2:
                    maxTimeDiff = max(min(table[i-1]), table[i-1][1] - temp[0])
                else:
                    maxTimeDiff = min(table[i - 1])
            for j in range(1, len(skill)):
                temp.append(temp[-1] + mana[i]*skill[j])
                if i > 0 and j < len(skill) - 1:
                    if table[i-1][j+1] - temp[j] > maxTimeDiff:
                        maxTimeDiff = table[i-1][j+1] - temp[j]
            # if i > 0:
            #     print(maxTimeDiff)
            if i > 0:
                for j in range(len(skill)):
                    temp[j] += maxTimeDiff
            table.append(temp)
        # print(table)
        return table[-1][-1]