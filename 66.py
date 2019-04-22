class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        digits[-1] += 1
        i = 1
        while i < length:
            if digits[-i] != digits[-i] % 10:
                digits[-i] %= 10
                digits[-i-1] += 1
                i += 1
            else:
                break
        if digits[0] != digits[0] % 10:
            digits[0] %= 10
            digits.insert(0, 1)
        return digits


def main():
    digits = [9, 9, 9]
    S = Solution()
    result = S.plusOne(digits)
    print(result)


if __name__ == '__main__':
    main()
