class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k > length:
            k %= length

        # # method 1 start
        # while k > 0:
        #     temp = nums[-1]
        #     i = 1
        #     while i < length:
        #         nums[-i] = nums[-i - 1]
        #         i += 1
        #     nums[0] = temp
        #     k -= 1
        # # method 1 end

        # method 2 start
        def reverse(start, end, array):
            while start < end:
                array[start] += array[end]
                array[end] = array[start] - array[end]
                array[start] -= array[end]
                start += 1
                end -= 1

        reverse(0, length - 1 - k, nums)
        reverse(length - k, length - 1, nums)
        reverse(0, length - 1, nums)
        # method 2 end


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    S = Solution()
    S.rotate(nums, k)
    print(nums)


if __name__ == '__main__':
    main()
