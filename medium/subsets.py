# https://leetcode.com/problems/subsets/
# Total subsets for an arr of len n is 2 power n
# Each subset is represented by binary representation of this total
# for ex. if n = 3
# total subsets is 8 viz. 2 power 3
# subset0 would be 000, subset1 = 001, subset2 = 010, subset3 = 011 and so on.
# if one is found in binary number then include num[index] where index is position of 1 in binary number
# for ex in 000 donot include any item in subset
# for 001 include only 3rd item (nums[2]) in subset
# for 010 include 2nd item (nums[1]) in subset
# 011 include 2nd and 3rd item (nums[1] and nums[2]) in subset

from typing import List

class Solution:
    def _getbinary(self, num):
        res: List[int] = []
        while num > 0:
            mod = num % 2
            res.append(mod)
            num = num // 2
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # init list
        res: List = []
        total= pow(2, len(nums))
        for i in range(total):
            bin_arr = self._getbinary(i)
            index: int = 0
            sub_set: List[int] = []
            while(index < len(bin_arr)):
                if (bin_arr[index] == 1):
                    sub_set.append(nums[index])
                index += 1
            res.append(sub_set)
        return res

if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))

