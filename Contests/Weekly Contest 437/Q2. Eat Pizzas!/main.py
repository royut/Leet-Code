class Solution(object):
    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        pizzas.sort()
        # print(pizzas)
        weightGained = 0
        days = len(pizzas) // 4
        oddDays = days // 2
        evenDays = days - oddDays
        # print(days, oddDays, evenDays)
        for i in range(evenDays):
            weightGained += pizzas.pop()
        for i in range(oddDays):
            pizzas.pop()
            weightGained += pizzas.pop()
        return weightGained


if __name__ == '__main__':
    print('in main')
    # pizzas = [1, 2, 3, 4, 5, 6, 7, 8]
    pizzas = [2, 1, 1, 1, 1, 1, 1, 1]
    # pizzas = [4,2,1,5,2,5,5,4,2,3,2,1]
    # pizzas = [5, 2, 2, 4, 3, 3, 1, 3, 2, 5, 4, 2]
    print(Solution().maxWeight(pizzas))
