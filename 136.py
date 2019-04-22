class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method 1 start
        # nums.sort()
        # length = len(nums)
        # i = 0
        # while i < length-2:
        #     if nums[i] != nums[i+1]:
        #         break
        #     else:
        #         i += 2
        # return nums[i]
        # method 1 end

        # method 2 start
        a = 0
        for num in nums:
            a = a ^ num
        return a
        # method 2 end


def main():
    nums = [1, 2, 2]
    S = Solution()
    result = S.singleNumber(nums)
    print(result)


if __name__ == '__main__':
    main()
