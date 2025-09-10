class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        cant = set()
        for i, j in friendships:
            temp = {}
            comFlag = False
            for lang in languages[i-1]:
                temp[lang] = 1
            for lang in languages[j-1]:
                if lang in temp:
                    comFlag = True
                    break
            if not comFlag:
                cant.add(i)
                cant.add(j)
        # print(cant)
        langCount = [0] * (n+1)
        maxCount = 0
        for f in cant:
            for lang in languages[f-1]:
                langCount[lang] += 1
                maxCount = max(maxCount, langCount[lang])
        return len(cant) - maxCount


if __name__ == '__main__':
    print('in main')
    # n = 2
    # languages = [[1], [2], [1, 2]]
    # friendships = [[1, 2], [1, 3], [2, 3]]
    n = 3
    languages = [[2], [1, 3], [1, 2], [3]]
    friendships = [[1, 4], [1, 2], [3, 4], [2, 3]]
    print(Solution().minimumTeachings(n, languages, friendships))