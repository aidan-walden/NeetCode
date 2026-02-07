/*
 * Problem: String Encode And Decode
 * URL: https://neetcode.io/problems/string-encode-and-decode
 * Date: 2026-02-06
 */

class Solution:

    DELIMITER = '#'

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length = len(string)
            encoded += f"{length}{self.DELIMITER}{string}"

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        pointer = 0
        len_cursor = ""
        while pointer < len(s):
            if s[pointer] == self.DELIMITER:
                read_length = int(len_cursor)
                pointer += 1 # Move past delimiter
                
                string_cursor = ""
                for i in range(pointer, pointer + read_length):
                    string_cursor += s[i]
                decoded.append(string_cursor)

                pointer += read_length
                len_cursor = ""
            else:
                len_cursor += s[pointer]
