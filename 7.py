class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x < -2**31) | (x > 2**31-1):
            return 0

        if x == abs(x):
            flag = 1
        else:
            flag = -1
        x = abs(x)
        x_reverse = 0
        while True:
            temp = x % 10
            x_reverse = x_reverse*10+temp
            if x == x % 10:
                break
            else:
                x = int(x/10)

        if (x_reverse < -2**31) | (x_reverse > 2**31-1):
            return 0

        return flag * x_reverse


def main():
    x = 120
    print(x)
    S = Solution()
    result = S.reverse(x)
    print(result)


if __name__ == '__main__':
    main()
