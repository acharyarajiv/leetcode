# https://leetcode.com/problems/integer-to-roman
class Solution:
    def intToRoman(self, num: int) -> str:
        int_nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        rom_nums = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        i = len(int_nums) - 1
        rom_op = ''
        while num > 0 and i >= 0:
            if num - int_nums[i] >= 0:
                rom_op += rom_nums[i]
                num -= int_nums[i]
            else:
                i -= 1
        return rom_op

if __name__ == '__main__':
    inputs = [3, 9, 4, 90, 900, 450, 800, 888, 444, 3999, 0]
    output = ['III', 'IX', 'IV', 'XC', 'CM', 'CDL', 'DCCC', 'DCCCLXXXVIII', 'CDXLIV', 'MMMCMXCIX', '']
    for index, inp in enumerate(inputs):
        actual = Solution().intToRoman(inp)
        expected = output[index]
        if actual == expected:
            pass
        else:
            print('Expected output: {}\nActual output: {}\n'.format(expected, actual))
