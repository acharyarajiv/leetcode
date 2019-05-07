class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        # append to output when i > 0 and stop append when i == 0
        i = 0
        res = ''
        for c in S:
            if c == '(':
                if i > 0:
                    res += c
                i += 1
            else:
                if i > 1:
                    res += c
                i -= 1
        return res


if __name__ == '__main__':
    inp_arr = ['(()())(())', '(()())(())(()(()))', '()()']
    out_arr = ['()()()', '()()()()(())', '']
    s = Solution()
    for index, value in enumerate(inp_arr):
        res = s.removeOuterParentheses(value)
        print('Input %s' % (value))
        print('Output\nExpected %s\nActual %s\n' % (out_arr[index], res))
