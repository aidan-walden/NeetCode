#
# Problem: Minimum Window Substring
# Difficulty: Hard
# URL: https://neetcode.io/problems/minimum-window-with-characters
# Date: 2026-03-03
#

from collections import deque

class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        # Approach: 2 pointers
        # Move right forward until all character requirements satisfied
        # Then, move left forward until satisfaction criteria is violated
        # Finally, move left backwards 1 to re-satisfy with smallest possible window

        t_counter = {}

        for char in t:
            if char in t_counter:
                t_counter[char] += 1
            else:
                t_counter[char] = 1

        right = 0

        best_window = s
        window_counter = {}
        window_deque = deque()
        ever_satisfied = False

        def check_satisfaction():
            nonlocal ever_satisfied
            nonlocal best_window
            nonlocal right

            satisfied = True
            for key in t_counter.keys():
                if key not in window_counter or window_counter[key] < t_counter[key]:
                    satisfied = False
                    break

            ever_satisfied = True if satisfied or ever_satisfied else False

            while satisfied:
                left_char = window_deque.popleft()

                if left_char not in t_counter:
                    continue

                char_condition = t_counter[left_char]

                new_left_char = window_counter[left_char] - 1

                if new_left_char < char_condition:
                    window_deque.appendleft(left_char)
                    break
                else:
                    window_counter[left_char] = new_left_char

            if not satisfied:
                if right_char in window_counter:
                    window_counter[right_char] += 1
                else:
                    window_counter[right_char] = 1

                window_deque.append(right_char)
                right += 1
            else:
                window_counter.clear()
                deque_len = len(window_deque)
                if deque_len < len(best_window):
                    best_window = ""
                    while len(window_deque) > 0:
                        best_window += window_deque.popleft()
                else:
                    window_deque.clear()
                right -= (deque_len - 1)

        while right < len(s):
            right_char = s[right]

            check_satisfaction()

        check_satisfaction()

        if not ever_satisfied:
            return ""

        return best_window
