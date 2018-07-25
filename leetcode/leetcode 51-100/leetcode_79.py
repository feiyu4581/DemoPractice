class Solution:
    def exist(self, board, word):
        if not board:
            return False

        if not word:
            return True

        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(row, col, board, word):
                    return True

        return False

    def dfs(self, row, col, board, word):
        if not word:
            return True

        if row < 0 or row >= len(board):
            return False

        if col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != word[0]:
            return False

        board[row][col] = '*'

        res = self.dfs(row + 1, col, board, word[1:]) or self.dfs(row - 1, col, board, word[1:]) or self.dfs(row, col + 1, board, word[1:]) or self.dfs(row, col - 1, board, word[1:])

        board[row][col] = word[0]

        return res


    def exist2(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        locations = {char: [] for char in word}
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in locations:
                    locations[board[row][col]].append([(row, col)])

        res = None
        for char in word:
            if not locations[char]:
                return False 

            if res is None:
                res = locations[char]
            else:
                new_res = []
                for prev_location in res:
                    for next_location in locations[char]:
                        offset = abs((next_location[0][0] - prev_location[-1][0])) + abs((next_location[0][1] - prev_location[-1][1]))
                        if offset == 1 and next_location[0] not in prev_location:
                            new_res.append(prev_location + next_location)

                if not new_res:
                    return False

                res = new_res

        return True
            

x = Solution()
print(x.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'ABCCED') == True)

print(x.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'SEE') == True)

print(x.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'ABCB') == False)

print(x.exist([
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","b"]
], 'aaaaaaaaaaaaaaaaaaaa') == False)
        