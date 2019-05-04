'''
can also be solved using stack
build stack containing chars from S which are a-z or A-Z
read String s from index 0, s.length and 
    if s[index] is a-z or A-Z stack pop and append to output
    else append s[index] to output
'''


class Solution(object):
    def isLetter(self, c):
        return c.isalpha()

    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ''
        s_len = len(S)
        curr_index, last_index = 0, s_len
        while curr_index < s_len:
            current_char = S[curr_index]
            # if current_char is a-z or A-Z then
            # find a valid char which is from a-z or A-Z and join
            # else join the spl in the same index

            if self.isLetter(current_char):
                while True:
                    last_index -= 1
                    last_char = S[last_index]
                    if self.isLetter(last_char):
                        res += last_char
                        break
            else:
                res += S[curr_index]
            curr_index += 1
        return res


if __name__ == '__main__':
    inp_arr = ['ab-cd', 'a-bC-dEf-ghIj', 'Test1ng-Leet=code-Q!']
    out_arr = ['dc-ba', 'j-Ih-gfE-dCba', 'Qedo1ct-eeLg=ntse-T!']
    s = Solution()
    for index, value in enumerate(inp_arr):
        res = s.reverseOnlyLetters(value)
        print('input s -> %s' % (value))
        print('output\nexpected \t%s\nactual \t%s\n' % (out_arr[index], res))
