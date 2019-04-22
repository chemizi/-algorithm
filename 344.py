class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        # method 1 start
        i = 0
        j = len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        # method 1 end

        # # method 2 start
        # return s[::-1]
        # # method 2 end


def main():
    s = ['a', 'b', 'c']
    print(s)
    S = Solution()
    S.reverseString(s)
    print(s)


if __name__ == '__main__':
    main()
