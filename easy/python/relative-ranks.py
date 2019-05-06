class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # clone num input
        nums_clone = nums[:]

        # create a map to store rank
        res_dict = {}
        for num in nums:
            res_dict[num] = ''

        # sort nums and update rank in map accordingly
        nums.sort(reverse = True)
        for index, num in enumerate(nums):
            if index == 0:
                res_dict[num] = 'Gold Medal'
            elif index == 1:
                res_dict[num] = 'Silver Medal'
            elif index == 2:
                res_dict[num] = 'Bronze Medal'
            else:
                res_dict[num] = str(index + 1)

        # nums_clone has input data in original order
        # create output with relative rank
        res = []
        for num in nums_clone:
            res.append(res_dict[num])
        return res


if __name__ == '__main__':
    inp_arr = [[5, 4, 3, 2, 1], [10, 3, 8, 9, 4]]
    out_arr = [["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"], ["Gold Medal","5","Bronze Medal","Silver Medal","4"]]
    s = Solution()
    for index, value in enumerate(inp_arr):
        res = s.findRelativeRanks(value)
        print('input s -> %s' % (value))
        print('output\nexpected \t%s\nactual \t%s\n' % (out_arr[index], res))
