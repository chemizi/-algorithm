class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            length = len(s)

        s_array = [_ for _ in s]
        t_array = [_ for _ in t]
        s_array.sort()
        t_array.sort()
        i = 0
        while i < length:
            if s_array[i] != t_array[i]:
                return False
            else:
                i += 1
        return True


def main():
    s = "cat"
    t = "tab"
    S = Solution()
    result = S.isAnagram(s, t)
    print(result)


if __name__ == '__main__':
    main()
