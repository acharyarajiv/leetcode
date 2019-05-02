'''
this can be solved by performing sum and diff based on path direction
or by pushing and poping 2 stacks (one for UD and one for LR)
'''


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        v_dist, h_dist = 0, 0

        for move in moves:
            if move == 'U':
                v_dist += 1
            elif move == 'D':
                v_dist -= 1
            elif move == 'L':
                h_dist += 1
            elif move == 'R':
                h_dist -= 1

        res = v_dist == 0 and h_dist == 0
        return res


if __name__ == '__main__':
    inp_arr = ['UD', 'LL']
    out_arr = [True, False]

    s = Solution()
    for index, value in enumerate(inp_arr):
        res = s.judgeCircle(value)
        print('input moves %s' % (value))
        print('output expected %s actual %s\n' % (out_arr[index], res))
