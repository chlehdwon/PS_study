# Given a non-negative integer numRows, generate the first numRows of
# Pascal's triangle.


# Brute Force. (O(n^2))

class Solution:
    def generate(self, numRows: int):
        triangle = [[1] for i in range(numRows)]
        for i in range(0, numRows-1):
            if i != 0:
                for j in range(0, i):
                    triangle[i+1].append(triangle[i][j]+triangle[i][j+1])
            triangle[i+1].append(1)
        return triangle


# Faster Algorithm. Uses -1 index. More efficient indexing.

class Solution2:
    def generate(self, numRows: int):
        pascal_tri = []
        for row in range(1, numRows+1):
            new_row = [1]*row
            for j in range(1, row-1):
                new_row[j] = pascal_tri[-1][j-1] + pascal_tri[-1][j]
            pascal_tri.append(new_row)
        return pascal_tri


a = Solution()
print(a.generate(1))
