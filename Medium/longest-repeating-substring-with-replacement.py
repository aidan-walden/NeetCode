#
# Problem: Longest Repeating Character Replacement
# Difficulty: Medium
# URL: https://neetcode.io/problems/longest-repeating-substring-with-replacement
# Date: 2026-03-03
#

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_freq = {}

        left = 0
        right = 0
        most_frequent = 1
        best_len = 0

        while right < len(s):
            char_right = s[right]
            if char_right in character_freq:
                freq = character_freq[char_right] + 1
                most_frequent = max(most_frequent, freq)
                character_freq[char_right] = freq
            else:
                character_freq[char_right] = 1

            window_size = right - left + 1
            
            while window_size - most_frequent > k:
                char_left = s[left]
                character_freq[char_left] -= 1
                left += 1
                window_size = right - left + 1
            right += 1

            best_len = max(best_len, window_size)

        return best_len
