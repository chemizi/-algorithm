class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 < length2:
            length_longer = length2
            length_shorter = length1
            nums_longer = nums2
            nums_shorter = nums1
        else:
            length_longer = length1
            length_shorter = length2
            nums_longer = nums1
            nums_shorter = nums2

        i = 0
        nums_intersect = []
        while i < length_shorter:
            j = 0
            while j < length_longer:
                if nums_shorter[i] == nums_longer[j]:
                    break
                else:
                    j += 1
            if j < length_longer:
                nums_intersect.append(nums_longer[j])
                nums_longer.remove(nums_longer[j])
                length_longer -= 1
            i += 1
        return nums_intersect


def main():
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    S = Solution()
    result = S.intersect(nums1, nums2)
    print(result)


if __name__ == '__main__':
    main()
