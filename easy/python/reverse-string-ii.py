class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        s_len = len(s)
        res = []
        # similar to for(i = 0; i< s.length; i = i + (2 * k))
        for i in range(0, s_len, (2*k)):
            # s.substring(i, k).reverse()
            res.append(s[i: (i+k)][::-1])
            # s.substring(i+k, i + (2 * k))
            res.append(s[(i+k): (i+(2*k))])
        # concetnate all string in res list (string join)
        return ''.join(res)


if __name__ == '__main__':
    inp_arr = [["abcde", 2], ['abcdefg', 2], ['a', 1], ['abcdefg', 8]]
    out_arr = ["bacde", 'bacdfeg', 'a', 'gfedcba']
    s = Solution()
    for index, value in enumerate(inp_arr):
        res = s.reverseStr(value[0], value[1])
        print('input\ns -> %s\tk -> %s' % (value[0], value[1]))
        print('output\nexpected \t%s\nactual \t%s\n' % (out_arr[index], res))
