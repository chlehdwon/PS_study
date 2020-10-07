# You are given an n x n 2D matrix representing an image,
# rotate the image by 90 degrees (clockwise)

# You have to rotate the image in-place, which means you have to modify
# the input 2D matrix directly. DO NOT allocate another 2D matrix and do
# the rotation.


class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix[0])
        for i in range(n//2):
            for j in range(i, n-i-1):
                print(matrix[i][j], matrix[j][n-1-i], matrix[n-i-1][n-j-1],
                      matrix[n-j-1][i])
                matrix[i][j], matrix[j][n-1-i], matrix[n-i-1][n-j-1],
                matrix[n-j-1][i] = matrix[n-j-1][i], matrix[i][j],
                matrix[j][n-1-i], matrix[n-i-1][n-j-1]
        print(matrix)


class Solution2:
    def rotate(self, matrix) -> None:
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for j in range(0, n):
            left = 0
            right = n-1
            while left < right:
                matrix[j][left], matrix[j][right] = matrix[j][right],
matrix[j][left]
                left += 1
                right -= 1


a = Solution()
a.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a.rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
