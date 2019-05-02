'''
solution is based on sliding window technique
'''


class Solution(object):
    # build char count map
    def charcountmap(self, string):
        char_map = {}
        for s in string:
            if s in char_map:
                char_map[s] += 1
            else:
                char_map[s] = 1
        return char_map

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        char_map = self.charcountmap(p)
        char_counter = len(char_map)
        s_len = len(s)
        start, end = 0, 0
        # print('char_map at init %s' % (char_map))
        while end < s_len:
            e = s[end]
            if e in char_map:
                char_map[e] -= 1
                if char_map[e] == 0:
                    char_counter -= 1
                    # print('char_map at end at char %s -> %s' % (char_map, e))
            end += 1

            while char_counter == 0:
                st = s[start]
                if st in char_map:
                    char_map[st] += 1
                    if char_map[st] > 0:
                        char_counter += 1
                        # print('char_map at start at char %s -> %s' % (char_map, st))
                        if end - start == len(p):
                            result.append(start)
                start += 1
        return result


if __name__ == '__main__':
    input_arr = [['cbaebabacd', 'abc'],
                ['abab', 'ab'],
                ['abaacbabc', 'abc'],
                ['baa', 'aa']]
    output_arr = [[0, 6], [0, 1, 2], [3, 4, 6], [1]]
    s = Solution()
    for index, inp in enumerate(input_arr):
        out = s.findAnagrams(inp[0], inp[1])
        print('input s = %s and p = %s' % (inp[0], inp[1]))
        print('output actual = %s expected = %s\n' % (out, output_arr[index]))
