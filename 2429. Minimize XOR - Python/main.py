class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        num1B2 = ""
        num2B2 = ""
        while num1 > 0:
            num1B2 = str(num1 % 2) + num1B2
            num1 = num1 // 2
        while num2 > 0:
            num2B2 = str(num2 % 2) + num2B2
            num2 = num2 // 2
        # print(num1B2, num2B2)
        count1Num1 = num1B2.count("1")
        count1Num2 = num2B2.count("1")
        diff = abs(count1Num2 - count1Num1)
        finalB2 = ""
        if count1Num2 > count1Num1:
            for i in range(len(num1B2)-1, -1, -1):
                # print(i ,'aaa', num1B2[i], finalB2)
                if num1B2[i] == "0":
                    if diff > 0:
                        diff -= 1
                        finalB2 = finalB2 + "1"
                    else:
                        finalB2 = finalB2 + "0"
                else:
                    finalB2 = finalB2 + "1"
            # print(finalB2)
            if diff > 0:
                for i in range(diff):
                    finalB2 = "1" + finalB2
        elif count1Num2 == count1Num1:
            finalB2 = num1B2[::-1]
        elif count1Num2 < count1Num1:
            for i in range(len(num1B2)-1, -1, -1):
                if num1B2[i] == "1":
                    if diff > 0:
                        diff -= 1
                        finalB2 = finalB2 + "0"
                    else:
                        finalB2 = finalB2 + "1"
                else:
                    finalB2 = finalB2 + "0"

        # print(finalB2)
        final = 0
        for i in range(len(finalB2)):
            final = final + pow(2, i) * int(finalB2[i])
        return final


if __name__ == '__main__':
    print('in main')
    num1 = 28
    num2 = 35
    print('s', Solution().minimizeXor(num1, num2))
