#
# Problem: Word Search
# Difficulty: Medium
# URL: https://neetcode.io/problems/search-for-word
# Date: 2026-03-27
#

class Solution:
    def _do_one(self, word: str, target_index_one: int, target_index_two: int, width: int, height: int):
        if target_index_one < 0 or target_index_two < 0 or target_index_one >= height or target_index_two >= width:
            return
        if len(self.current_word) == len(word):
            return
        coords = (target_index_one, target_index_two)
        if coords in self.visited:
            return
        
        this_char = self.board[target_index_one][target_index_two]
        word_index = len(self.current_word)

        did_append = False

        if this_char == word[word_index]:
            self.current_word += this_char
            did_append = True
            self.visited[coords] = True

        if not did_append:
            return

        # path 1: go up
        self._do_one(word, target_index_one - 1, target_index_two, width, height)

        # path 2: go down
        self._do_one(word, target_index_one + 1, target_index_two, width, height)

        # path 3: go left
        self._do_one(word, target_index_one, target_index_two - 1, width, height)

        # path 4: go right
        self._do_one(word, target_index_one, target_index_two + 1, width, height)

        if len(self.current_word) == len(word):
            return
        self.current_word = self.current_word[:-1]
        del self.visited[coords]
        

    def exist(self, board: List[List[str]], word: str) -> bool:
            self.board = board

            height = len(board)
            width = len(board[0])

            cur_height = 0
            cur_width = 0

            # we must try from every starting position in the board
            while cur_height < height:
                self.visited = {}
                self.current_word = ""
                self._do_one(word, cur_height, cur_width, width, height)

                if self.current_word == word:
                    return True

                if cur_width == width - 1:
                    cur_height += 1
                    cur_width = 0
                else:
                    cur_width += 1

            return False

