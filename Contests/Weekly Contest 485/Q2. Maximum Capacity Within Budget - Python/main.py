class Solution(object):
    def maxCapacity(self, costs, capacity, budget):
        """
        :type costs: List[int]
        :type capacity: List[int]
        :type budget: int
        :rtype: int
        """
        pairs = []
        for i in range(len(costs)):
            pairs.append([costs[i], capacity[i]])
        pairs.sort(key=lambda x: x[0])
        print(pairs)


if __name__ == "__main__":
    print('in main')
    costs = [4, 8, 5, 3]
    capacity = [1, 5, 2, 7]
    budget = 8
    print(Solution().maxCapacity(costs, capacity, budget))
