class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # one liner solution
        # return ' '.join(''.join(c for c in word[::-1]) for word in s.split(' '))
        res = ''
        for word in s.split(' '):
            '''
                below for is similar to 
                for (int i = word.length; i > -1; i--){
                    char c = word[i]
                }
            '''
            for c in word[::-1]:
                res += c
            res += ' '
        # similar to res.substring(0, res.length)
        return res[0:len(res)-1]


if __name__ == '__main__':
    inp_arr = ["Let's take LeetCode contest"]
    out_arr = ["s'teL ekat edoCteeL tsetnoc"]
    s = Solution()
    for index, value in enumerate(inp_arr):
        res = s.reverseWords(value)
        print('input s %s' % (value))
        print('output\nexpected \t%s\nactual \t%s\n' % (out_arr[index], res))
