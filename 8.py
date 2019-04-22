class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_split = str.split()
        print(str_split)
        if len(str_split) == 0:
            return 0
        str_first = str_split[0]
        flag = 1
        if (str_first[0] != "-") & (str_first[0] != "+") & (str_first[0] < "0") & (str_first[0] > "9"):
            return 0
        if str_first[0] == "-":
            flag = -1
            str_first = str_first[1:]
        elif str_first[0] == "+":
            flag = 1
            str_first = str_first[1:]

        print(str_first)

        length = len(str_first)
        i = 0
        num = 0
        while i < length:
            if (str_first[i] >= "0") & (str_first[i] <= "9"):
                num = num*10+(ord(str_first[i])-ord("0"))
                if (num >= 2**31-1) | (num <= -2**31):
                    return -2147483648
                i += 1
            else:
                return flag*num
        return flag*num


def main():
    s = "+3.1413"
    S = Solution()
    result = S.myAtoi(s)
    print(result)


if __name__ == '__main__':
    main()
