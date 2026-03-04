#
# Problem: Valid Parentheses
# Difficulty: Easy
# URL: https://neetcode.io/problems/validate-parentheses
# Date: 2026-03-03
#

class Solution:
    def isValid(self, s: str) -> bool:
        paren_key = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for char in s:
            if len(stack) == 0:
                if char not in paren_key:
                    # The first character of the string is a closing bracket
                    return False
                stack.append(char)
            else:
                if char in ')]}':
                    corresponding_opening = stack.pop()
                    if paren_key[corresponding_opening] != char:
                        return False
                else:
                    stack.append(char)

        return len(stack) == 0
            
