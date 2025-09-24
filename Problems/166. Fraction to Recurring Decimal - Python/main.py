class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        negative = False
        if numerator < 0 and denominator < 0:
            numerator = -numerator
            denominator = -denominator
        elif numerator > 0 and denominator > 0:
            pass
        else:
            numerator = abs(numerator)
            denominator = abs(denominator)
            negative = True
        D = numerator // denominator
        R = numerator % denominator
        fstr = str(D)
        if R == 0:
            if negative:
                fstr = '-' + fstr
            return fstr
        remainders = {}
        stack = []
        repeatFlag = False
        while R != 0:
            R *= 10
            d = R // denominator
            r = R % denominator
            stack.append((d, r))
            if d in remainders:
                if r in remainders[d]:
                    repeatFlag = True
                    repeatPair = (d, r)
                    stack.pop()
                    break
                else:
                    remainders[d].append(r)
            else:
                remainders[d] = [r]
            # print(d, r)
            R = r
        fstr += '.'
        repeatStr = '('
        # print(stack)
        inRepeat = False
        for i in range(len(stack)):
            if (repeatFlag and stack[i] == repeatPair) or inRepeat:
                inRepeat = True
                repeatStr += str(stack[i][0])
            else:
                fstr += str(stack[i][0])
        if repeatFlag:
            fstr += repeatStr + ')'
        if negative:
            fstr = '-' + fstr
        return fstr


if __name__ == '__main__':
    print('in main')
    numerator = 4
    denominator = 333
    numerator = -50
    denominator = 8
    print(Solution().fractionToDecimal(numerator, denominator))