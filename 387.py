class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = [_ for _ in s]
        temp = {}
        for i, letter in enumerate(s_list):
            if letter in temp:
                temp[letter] = len(s_list)
            else:
                temp[letter] = i

        min_i = len(s_list)
        print(temp)
        for j in temp:
            min_i = min(min_i, temp[j])

        if min_i == len(s_list):
            return -1
        else:
            return min_i


def main():
    s = "aadadaad"
    S = Solution()
    result = S.firstUniqChar(s)
    print(result)


if __name__ == '__main__':
    main()
