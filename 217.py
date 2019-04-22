class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # method 1 start
        nums.sort()
        length = len(nums)
        i = 0
        while i < length - 1:
            if nums[i] == nums[i + 1]:
                break
            i += 1
        if i < length - 1:
            return True
        else:
            return False
        # method 1 end

        # # method 2 start
        # return len(nums) != len(set(nums))
        # # method 2 end


def main():
    nums = [1, 3, 2]
    S = Solution()
    result = S.containsDuplicate(nums)
    print(result)


if __name__ == '__main__':
    main()
