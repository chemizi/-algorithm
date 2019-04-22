class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # method 1 start
        length = len(prices)
        profit = 0
        for i in range(1, length):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
        # method 1 end


def main():
    prices = [8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]
    S = Solution()
    result = S.maxProfit(prices)
    print(result)


if __name__ == '__main__':
    main()
