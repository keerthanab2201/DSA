class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # if current cell matches current char- move to its 4 neighbours to check next character
        # if a path fails, we undo/backtrack to try other paths
        # mark current cell as visited in a hashset
        rows= len(board)
        columns= len(board[0])
        visited= set()
        def dfs(row,column,i):
            if i==len(word):
                return True
            # ensure current cell is within bounds, its char matches that of the word, and no cell is visited more than once
            if min(row,column)<0 or row>=rows or column>=columns or word[i]!=board[row][column] or (row,column) in visited:
                return
            visited.add((row,column))
            res= dfs(row+1, column, i+1) or dfs(row-1, column, i+1) or dfs(row, column+1, i+1) or dfs(row, column-1, i+1)
            visited.remove((row,column))
            return res
        
        for r in range(rows):
            for c in range(columns):
                if dfs(r,c,0):
                    return True
        return False

'''Am I trying to generate every solution, or am I just checking if one solution exists?
Generate all solutions → Explore every branch (separate recursive calls or loops).
Check whether at least one solution exists → Combine recursive calls with or (or any(...)) so you can stop early. '''