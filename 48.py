class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        def fourrotate(matrix, i, j):
            sumvalue = len(matrix[0])-1
            matrix[i][j], matrix[j][sumvalue-i], matrix[sumvalue-i][sumvalue-j], matrix[sumvalue-j][i]\
                = matrix[sumvalue-j][i], matrix[i][j], matrix[j][sumvalue-i], matrix[sumvalue-i][sumvalue-j]

        def getint(num):
            num = int((num*10+5)/10)
            return num

        for i in range(int(len(matrix[0])/2)):
            for j in range(getint(len(matrix[0])/2)):
                fourrotate(matrix, i, j)


def main():
    matrix = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
    print(matrix)
    S = Solution()
    S.rotate(matrix)
    print(matrix)


if __name__ == '__main__':
    main()
