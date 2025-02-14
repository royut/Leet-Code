class ProductOfNumbers(object):

    def __init__(self):
        self.products = []
        self.lastZeroIndex = -1

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.products) == 0:
            if num == 0:
                self.products.append(1)
                self.lastZeroIndex = len(self.products) - 1
            else:
                self.products.append(num)
        else:
            if num == 0:
                self.products.append(self.products[-1] * 1)
                self.lastZeroIndex = len(self.products) - 1
            else:
                self.products.append(self.products[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if len(self.products) - self.lastZeroIndex <= k:
            return 0
        if len(self.products) == k:
            return self.products[-1]
        return int(self.products[-1] / self.products[-k - 1])


if __name__ == '__main__':
    print('in main')
    # Your ProductOfNumbers object will be instantiated and called as such:
    obj = ProductOfNumbers()
    # obj.add(3)
    # print(obj.getProduct(1))
    # obj.add(0)
    # obj.add(2)
    # obj.add(5)
    # obj.add(4)
    # print(obj.getProduct(2))
    # print(obj.getProduct(3))
    # print(obj.getProduct(4))
    # obj.add(8)
    # print(obj.getProduct(2))
    obj.add(7)
    print(obj.getProduct(1))
    # obj.add(0)
    # obj.add(9)
    # print(obj.getProduct(3))
    # obj.add(8)
    # obj.add(3)
    # obj.add(8)
    # print(obj.getProduct(5))
    # print(obj.getProduct(4))
    # print(obj.getProduct(6))