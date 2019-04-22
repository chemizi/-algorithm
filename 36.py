class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # method 1 start
        def findsame(nums):
            length = len(nums)
            nums_copy = nums.copy()
            nums_copy.sort()
            for i in range(length-1):
                if (nums_copy[i] == nums_copy[i+1]) & (nums_copy[i] != "."):
                    return True
                else:
                    i += 1

        steps = len(board)
        flag = False
        print(steps)
        for i in range(steps):
            if findsame(board[i]):
                flag = True

        for i in range(steps):
            nums_col = []
            for j in range(steps):
                nums_col.append(board[j][i])
            if findsame(nums_col):
                flag = True

        for i in range(3):
            for j in range(3):
                nums_square = []
                for k in range(3):
                    for p in range(3):
                        nums_square.append(board[i*3+k][j*3+p])
                if findsame(nums_square):
                    flag = True

        return not flag  # flag表示是否有重复, not flag 表示是否满足数独条件
        # method 1 end

        # method 2 start
        # for row in board:
        #     if len(set(row)) + row.count('.') != 10:
        #         return False
        # for col in zip(*board):
        #     if len(set(col)) + col.count('.') != 10:
        #         return False
        # for i in [0, 3, 6]:
        #     for j in [0, 3, 6]:
        #         squ = board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]
        #         if len(set(squ)) + squ.count('.') != 10:
        #             return False
        # return True
        # method 2 end


def main():
    board = [
        [".",".",".",".",".",".",".",".","2"],
        [".",".",".",".",".",".","6",".","."],
        [".",".","1","4",".",".","8",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".","3",".",".",".","."],
        ["5",".","8","6",".",".",".",".","."],
        [".","9",".",".",".",".","4",".","."],
        [".",".",".",".","5",".",".",".","."]]
    S = Solution()
    result = S.isValidSudoku(board)
    print(result)


if __name__ == '__main__':
    main()
