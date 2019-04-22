class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n -= 1

        def count(x):
            result = ""
            length = len(x)
            i = 0
            while i < length:
                j = 0
                while ((i+j) < length):
                    if (x[i+j] != x[i]):
                        break
                    j += 1
                result += ((chr(j+ord("0")))+x[i])
                i += j
            return result

        i = 1
        num = []
        num.append("1")
        while i <= n:
            print(count(num[i-1]))
            num.append(count(num[i-1]))
            i += 1
        return num[n]


def main():
    n = 5
    S = Solution()
    result = S.countAndSay(n)
    print(result)


if __name__ == '__main__':
    main()
