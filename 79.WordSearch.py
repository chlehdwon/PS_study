# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent
# cells, where "adjacent" cells are horizontally or vertically
# neighboring. The same letter cell may not be used more than once.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board,i,j,count,word):
            if(count == len(word)):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or word[count]!=board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = ""
            found = dfs(board,i+1,j,count+1,word) or dfs(board,i-1,j,count+1,word) or dfs(board,i,j+1,count+1,word) or dfs(board,i,j-1,count+1,word)
            board[i][j] = temp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(board,i,j,0,word):
                    return True
        return False


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])
        
        def backtrack(i, j, idx):
            char = board[i][j]
            if char != word[idx]:
                return False
            elif idx == len(word)-1:
                return True
            
            board[i][j] = ''
            
            if i > 0 and backtrack(i-1, j, idx+1):
                return True
            if j > 0 and backtrack(i, j-1, idx+1):
                return True
            if i < nrows-1 and backtrack(i+1, j, idx+1):
                return True
            if j < ncols-1 and backtrack(i, j+1, idx+1):
                return True            
            board[i][j] = char
            return False
                    
        for i in range(nrows):
            for j in range(ncols):
                if backtrack(i, j, 0):
                    return True
            
        return False


a = Solution()
print(a.exist([["C","A","A"],["A","A","A"],["B","C","D"]],
"AAB"))
