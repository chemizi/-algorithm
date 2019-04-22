class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_array = []
        j = 0
        for i in s:
            if (i >= "a") & (i <= "z"):
                s_array.append(i)
            elif (i >= "A") & (i <= "Z"):
                s_array.append(chr(ord(i)-ord("A")+ord("a")))
            elif (i >= "0") & (i <= "9"):
                s_array.append(i)
        # print(s_array)

        i = 0
        j = len(s_array)-1
        while i < j:
            if s_array[i] != s_array[j]:
                return False
            i += 1
            j -= 1
        return True



def main():
    s = "0P"
    S = Solution()
    result = S.isPalindrome(s)
    print(result)


if __name__ == '__main__':
    main()
