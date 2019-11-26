# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = []
        max_length = 0
        j = 0
        while j < len(s):
            if s[j] in char_set:
                # if already present then upto previous char
                # in case of string abcdc
                # then remove ab from char_set
                max_length = max(max_length, len(char_set))
                while True:
                    if char_set[0] == s[j]:
                        char_set.pop(0)
                        break
                    char_set.pop(0)
            char_set.append(s[j])
            j += 1

        max_length = max(max_length, len(char_set))
        return max_length


if __name__ == '__main__':
    inputs = ['abcabcbb', 'bbbb', 'pwwkew', 'dvdf', 'aabaab!bb']
    output = [3, 1, 3, 3, 3]
    for index, input_str in enumerate(inputs):
        actual = Solution().lengthOfLongestSubstring(input_str)
        expected = output[index]
        if actual == expected:
            pass
        else:
            print('Expected output: {}\nActual output: {}\n'.format(expected, actual))

