# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List

class Solution:
    def _swap(self, nums, src, dest):
        tmp = nums[src]
        nums[src] = nums[dest]
        nums[dest] = tmp

    def removeDuplicates(self, nums: List[int]) -> int:
        current_index: int = 0
        next_index: int = 1
        count: int = 0
        while next_index < len(nums):
            if nums[current_index] == nums[next_index]:
                count += 1
            else:
                count = 0

            if count > 1:
                # duplicate count is more than 1 then increment next_index
                pass
            elif current_index + 1 < next_index:
                # if current_index and next are not next to each other and duplicate count is < 1 then swap non dup elem with current one
                current_index += 1
                self._swap(nums, current_index, next_index)
            else:
                # duplicate count is <= 1 then if current_index is next to next_index then make next_index as current_index
                current_index = next_index
            next_index += 1

        return current_index + 1

if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,1,1,2,2,2,3]))

