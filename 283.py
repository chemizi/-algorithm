class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
            i += 1
        for j in range(count, length):
            nums[j] = 0


def main():
    nums = [1, 2, 0, 1]
    S = Solution()
    S.moveZeroes(nums)
    print(nums)


if __name__ == '__main__':
    main()
