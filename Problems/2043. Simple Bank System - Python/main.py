class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = {}
        for i in range(len(balance)):
            self.balance[i+1] = balance[i]
        self.accountNum = len(balance)
        # print(self.balance, self.accountNum)

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        # print(self.balance[account1])
        if account1 > self.accountNum or account2 > self.accountNum:
            return False
        if self.balance[account1] < money:
            return False
        else:
            self.balance[account1] -= money
            self.balance[account2] += money
            # print(self.balance)
            return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account > self.accountNum:
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account > self.accountNum:
            return False
        if self.balance[account] < money:
            return False
        else:
            self.balance[account] -= money
            return True


if __name__ == '__main__':
    print('in main')
    # Your Bank object will be instantiated and called as such:
    balance = [10, 100, 20, 50, 30]
    obj = Bank(balance)
    print(obj.withdraw(3, 10))
    # param_2 = obj.deposit(account,money)
    # param_3 = obj.withdraw(account,money)