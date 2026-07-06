class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        freq_check = {}
        
        for i in range(9):
            freq_check = Counter(board[i])
            for key, value in freq_check.items():
                if key.isdigit() and freq_check[key] != 1:
                    return False
        
        for i in range(9):
            new_board = [row[i] for row in board]
            freq_check = Counter(new_board)
            for key, value in freq_check.items():
                if key.isdigit() and freq_check[key] != 1:
                    return False
        
        square = {}
        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == ".":
                    continue

                zip_code = (r // 3, c // 3)
                if zip_code not in square:
                    square[zip_code] = set()

                if char in square[zip_code]:
                    return False

                square[zip_code].add(char)
        return True


