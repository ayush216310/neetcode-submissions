class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        fcount = 0
        for n in nums:
            if n-1 not in nums:
                length = 1
            
                while n+length in nums_set:
                    length += 1

                fcount = max(fcount, length)
        return fcount

            
        