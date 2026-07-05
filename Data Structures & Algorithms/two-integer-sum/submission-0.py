class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_ind = {}

        for index, n in enumerate(nums):
            complement = target - n

            if complement in comp_ind:
                return[comp_ind[complement], index]
            comp_ind[n] = index