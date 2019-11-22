# https://leetcode.com/problems/word-search/
# backtrack problem https://en.wikipedia.org/wiki/Backtracking
# Backtracking https://www.youtube.com/watch?v=DKCbsiDBN6c

from typing import List, Tuple

class Solution:
    def __exists(self, board: List[List[str]], index: Tuple[int, int], char: str, visited: List[List[int]]) -> bool:
        x, y = index
        # if -1 < x < board rows
        # if -1 < y < board cols
        # if not already visited
        # if is same charecter
        # return true
        # else false
        if x >= 0 and y >= 0 and x < len(board) and y < len(board[x]) and visited[x][y] == 0 and board[x][y] == char:
            return True
        else:
            return False

    def __checkIfExist(self, board: List[List[str]], index: Tuple[int, int], word: str, word_index: int,
                       visited: List[List[int]]) -> bool:
        # if word_index reached limit then all chars are found
        if word_index == len(word):
            return True

        # directions are upper cell (North) and down cell (South) of same column and right(east) and left(west) cell of same row
        directions: List[Tuple[int, int]] = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
        res: bool = False
        #for each direction loop and backtrack
        for direction in directions:
            row, col = index
            new_index = (row + direction[0], col + direction[1])
            # if exists then mark the cell as visited
            if self.__exists(board, new_index, word[word_index], visited):
                row, col = new_index
                visited[row][col] = 1
                # proceed to next charecter in word
                res = self.__checkIfExist(board, new_index, word, word_index + 1, visited)
                # backtrack
                visited[row][col] = 0
            if res:
                break
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        found: bool = False
        visited = [0] * len(board)
        for row in range(len(visited)):
            visited[row] = [0] * len(board[row])

        for row in range(len(board)):
            for col in range(len(board[row])):
                found = self.__checkIfExist(board, (row, col), word, 0, visited)
                if found:
                    break
            if found:
                break
        return found

def validate(res: bool, msg: str):
    if not res:
        print(msg)

if __name__ == '__main__':
    board = [
         ['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']
    ]
    validate(Solution().exist(board, 'ABCCED'), 'Should return true for input ABCCED')
    validate(Solution().exist(board, 'SEE'), 'Should return true for input SEE')
    validate(not Solution().exist(board, 'ABCB'), 'Should return false for input ABCB')

    board = [['A']]
    validate(Solution().exist(board, 'A'), 'Should return true for input A')
