class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if length == 0:
            return ""
        length_min = len(strs[0])
        index_min = 0
        for i in range(length):
            length_min = min(length_min, len(strs[i]))
            if length_min == len(strs[i]):
                index_min = i
        # print(index_min, length_min)

        flag = True
        for i in range(length_min):
            for j in range(length):
                if strs[j][i] != strs[index_min][i]:
                    flag = False
                    break
            if not flag:
                length_longest = i
                break
        if flag:
            length_longest = length_min
        return (strs[index_min][0:length_longest])


def main():
    strs = ["flower", "for", "flight"]
    S = Solution()
    result = S.longestCommonPrefix(strs)
    print(result)


if __name__ == '__main__':
    main()
