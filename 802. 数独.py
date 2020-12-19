class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        # write your code here
        used = self.initial_used(board)
        self.dfs(board, 0, used)
    
    def initial_used(self, board):
        # Each needs to be unique
        used = {
            'row': [set() for _ in range(9)],
            'col': [set() for _ in range(9)],
            'box': [set() for _ in range(9)],
        }
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    continue
                used['row'][i].add(board[i][j])
                used['col'][j].add(board[i][j])
                used['box'][i // 3 * 3 + j // 3].add(board[i][j])
        
        return used
        
    def is_valid(self, i, j, val, used):
        if val in used['row'][i]:
            return False
        if val in used['col'][j]:
            return False
        if val in used['box'][i // 3 * 3 + j // 3]:
            return False
        return True
        
    def dfs(self, board, index, used):
        if index == 81:
            return True
        i, j = index // 9, index % 9
        if board[i][j] != 0:
            return self.dfs(board, index+1, used)
        
        for val in range(1, 10):
            if not self.is_valid(i, j, val, used):
                continue
            
            board[i][j] = val
            used['row'][i].add(val)
            used['col'][j].add(val) 
            used['box'][i // 3 * 3 + j // 3].add(val)
        
            if self.dfs(board, index+1, used):
                return True
            
            used['box'][i // 3 * 3 + j // 3].remove(val)
            used['col'][j].remove(val)
            used['row'][i].remove(val)
            board[i][j] = 0 
        return False 
            
                
                
                
                
        