# https://leetcode.com/problems/reach-a-number/discuss/112986/Concise-Python-with-explanation-and-example


class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        step = 0
        sum_res = 0
        while sum_res < target:
            step += 1
            sum_res += step

        while ((sum_res - target) % 2 != 0):
            step += 1
            sum_res += step
        return step


if __name__ == '__main__':
    inp_arr = [3, 2, 9, -2]
    out_arr = [2, 3, 5, 3]
    s = Solution()
    for index, value in enumerate(inp_arr):
        res = s.reachNumber(value)
        print('input s -> %s' % (value))
        print('output\nexpected \t%s\nactual \t%s\n' % (out_arr[index], res))
