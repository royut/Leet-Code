import heapq


class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        impacts = []
        for i in range(len(classes)):
            impacts.append((-(float(classes[i][1] - classes[i][0]) / float(classes[i][1] * (classes[i][1] + 1))), i))
        heapq.heapify(impacts)

        for j in range(extraStudents):
            _, i = (heapq.heappop(impacts))
            classes[i][0] += 1
            classes[i][1] += 1
            tempGain = float(classes[i][1] - classes[i][0]) / float(classes[i][1] * (classes[i][1] + 1))
            heapq.heappush(impacts, (-tempGain, i))
        # print(classes)
        temp = 0
        for class_ in classes:
            temp += float(class_[0]) / float(class_[1])
        return float(temp) / float(len(impacts))


if __name__ == '__main__':
    print('in main')
    classes = [[1, 2], [3, 5], [2, 2]]
    extraStudents = 2
    # classes = [[2,4],[3,9],[4,5],[2,10]]
    # extraStudents = 4
    print(Solution().maxAverageRatio(classes, extraStudents))