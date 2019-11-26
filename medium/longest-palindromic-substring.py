# https://leetcode.com/problems/longest-palindromic-substring/
# case1 aba
# case2 bb
# Better way of handling palindrome is using ManachersAlgorithm
# this is brute force

from typing import List

class Solution:
    # case 1
    def __palindromeNeighbours(self, s, index):
        if index >= 1 and index < len(s) - 1 and s[index - 1] == s[index + 1]:
            return True
        else:
            return False

    # case 2
    def __palindromeSuccessor(self, s, index):
        if index >= 0 and index < len(s) - 1 and s[index] == s[index + 1]:
            return True
        else:
            return False


    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len == 0:
            return ''
        elif s_len == 1:
            return s

        j, max_len = 0, -1
        palindrome_str = ''
        while j < s_len:
            if self.__palindromeNeighbours(s, j):
                start_index, end_index = j, j
                while start_index >= 0 and end_index < s_len and s[start_index] == s[end_index]:
                    start_index -= 1
                    end_index += 1
                if (max_len < end_index - start_index + 1):
                    max_len = end_index - start_index + 1
                    palindrome_str = s[start_index + 1: end_index]

            if self.__palindromeSuccessor(s, j):
                start_index, end_index = j, j + 1
                while start_index >= 0 and end_index < s_len and s[start_index] == s[end_index]:
                    start_index -= 1
                    end_index += 1
                if (max_len < end_index - start_index + 1):
                    max_len = end_index - start_index + 1
                    palindrome_str = s[start_index + 1: end_index]
            j += 1

        if max_len == -1:
            return s[0]
        return palindrome_str


if __name__ == '__main__':
    input_s = ['a', 'aa', 'bbb', 'abb', 'bba', 'aba', 'abab', 'abcba', 'abcbabcba', 'ac', '']
    op_s = ['a', 'aa', 'bbb', 'bb', 'bb', 'aba', 'aba', 'abcba', 'abcbabcba', 'a', '']
    for index, s in enumerate(input_s):
        actual = Solution().longestPalindrome(s)
        expected = op_s[index]
        if actual == expected:
            pass
        else:
            print('Expected output: {}\nActual output: {}\n'.format(expected, actual))
