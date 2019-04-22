class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index, num in enumerate(nums):
            if target-num in d:
                return [d[target-num], index]
            d[num] = index


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 9
    S = Solution()
    result = S.twoSum(nums, target)
    print(result)


if __name__ == '__main__':
    main()
