class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        ordered = []
        for p in order:
            if p in friends:
                ordered.append(p)
        return ordered


if __name__ == "__main__":
    # order = [3, 1, 2, 5, 4]
    # friends = [1, 3, 4]
    order = [1, 4, 5, 3, 2]
    friends = [2, 5]
    print(Solution().recoverOrder(order, friends))