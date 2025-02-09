class Solution(object):
    def assignElements(self, groups, elements):
        """
        :type groups: List[int]
        :type elements: List[int]
        :rtype: List[int]
        """
        output = []
        eles = {}
        for i in range(len(elements)):
            if elements[i] not in eles:
                eles[elements[i]] = i
        for i in range(len(groups)):
            last = -1
            for ele in eles:
                if groups[i] % ele == 0:
                    last = eles[ele]
                    break
            output.append(last)
        return output


if __name__ == '__main__':
    print('in main')
    groups = [8,4,3,2,4]
    elements = [4,2]
    # groups = [2, 3, 5, 7]
    # elements = [5, 3, 3]
    # groups = [10, 21, 30, 41]
    # elements = [2, 1]
    # groups = [5]
    # elements = [6,6,5]
    print(Solution().assignElements(groups, elements))
