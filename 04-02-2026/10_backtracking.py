# Back Tracking Implementation
# Word Search
# Given a m x n board of characters and a word, return true if the word exists
# in the grid, where the word is constructed from letters in adjacent cells
# but cannot reuse the same letter cell more than once
def exist(board: list[list[str]], word: str) -> bool:
    def dfs(i, j, word_i):
        if board[i][j] != word[word_i]:
            return False
        if word_i == len(word) - 1:
            return True
        char = board[i][j]
        board[i][j] = "*"
        coords = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for r, c in coords:
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                if dfs(r, c, word_i + 1):
                    return True
        board[i][j]= char
        
    for r in  range(len(board)):
        for c in range(len(board)):
            if dfs(r, c, 0):
                return True
    return False

if __name__ == "__main__":
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E'],
    ]
    
    print("Backtracking Implementation")
    for row in board:
        print(row)
    print('Does "ASADFBC" exist in this board?',exist(board, 'ASADFBC'))