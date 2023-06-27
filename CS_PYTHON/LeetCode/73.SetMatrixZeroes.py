# Given an m x n matrix. If an element is 0,
# set its entire row and column to 0.
# Do it in-place.


class Solution:
    def setZeroes(self, matrix):

        column = []
        row = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    column.append(j)
        for l in range(len(row)):
            for j in range(len(matrix[0])):
                matrix[row[l]][j] = 0
        for k in range(len(column)):
            for i in range(len(matrix)):
                matrix[i][column[k]] = 0


class Solution2:
    def markInAllDir(self, i, j, matrix):
        x = i
        y = j
        # go right
        while x < len(matrix):
            if matrix[x][y] != 0:
                matrix[x][y] = "v"
            x += 1
        x = i
        y = j
        # go left
        while x >= 0:
            if matrix[x][y] != 0:
                matrix[x][y] = "v"
            x -= 1
        x = i
        y = j
        # go up
        while y >= 0:
            if matrix[x][y] != 0:
                matrix[x][y] = "v"
            y -= 1
        x = i
        y = j
        # go down
        while y < len(matrix[0]):
            if matrix[x][y] != 0:
                matrix[x][y] = "v"
            y += 1

    def setZeroes(self, matrix) -> None:
        for i, mat in enumerate(matrix):
            for j, v in enumerate(mat):
                if v == 0:
                    self.markInAllDir(i, j, matrix)
        print(matrix)
        for i, mat in enumerate(matrix):
            for j, v in enumerate(mat):
                if v == "v":
                    matrix[i][j] = 0


a = Solution2()
a.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])


