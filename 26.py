class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method 1 start
        for i in range(len(nums)):
            for j in range(len(nums)-i-2):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        # method 1 end

        # method 2 start
        nums.sort()  # 排序
        # method 2 end

        i = 0
        length = len(nums)
        while i < length-1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
                length = length-1
            else:
                i = i+1
        return len(nums)


def main():
    nums = [1, 1, 1, 2, 2, 3, 4, 3, 1, 2]
    S = Solution()
    result = S.removeDuplicates(nums)
    print(nums)
    print(result)


if __name__ == '__main__':
    main()
