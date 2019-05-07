'''
instead of checking for what overlaps its easier to check what donot overlap
overlap donot occur when
for x1, y1, x2, y2 are the point in rectangle rec1 and rec2 then
if rec1.x2 <= rec2.x1 
    or rec1.y2 <= rec2.y1
    or rec2.x2 <= rec1.x1
    or rec2.y2 <= rec1.y1
then rec1 and rec2 donot overlap
else rectangles overlap
'''


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return (not(rec1[2] <= rec2[0]
            or rec1[3] <= rec2[1]
            or rec2[2] <= rec1[0]
            or rec2[3] <= rec1[1])
        )


if __name__ == '__main__':
    inp_arr = [[[0,0,2,2], [1,1,3,3]], [[0,0,1,1], [1,0,2,1]]]
    out_arr = [True, False]
    s = Solution()
    for index, value in enumerate(inp_arr):
        res = s.isRectangleOverlap(value[0], value[1])
        print('input s -> %s' % (value))
        print('output\nexpected \t%s\nactual \t%s\n' % (out_arr[index], res))
