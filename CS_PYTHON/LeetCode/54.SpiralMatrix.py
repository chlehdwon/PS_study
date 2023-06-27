class Solution:
    def strip_matrix(self, matrix):
        return [[i for i in row[1:-1]] for row in matrix[1:-1]]

    def spiralOrder(self, matrix):
        if not matrix:
            return matrix
        row = len(matrix)
        if row < 2:
            return matrix[0]
        columns = len(matrix[0])
        if columns == 1:
            return [row[0] for row in matrix]

        return matrix[0] + \
            [row[-1] for row in matrix[1:-1]] + \
            matrix[-1][::-1] + \
            [row[0] for row in matrix[1:-1]][::-1] + \
            self.spiralOrder(self.strip_matrix(matrix))


a = Solution()
print(a.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]))
