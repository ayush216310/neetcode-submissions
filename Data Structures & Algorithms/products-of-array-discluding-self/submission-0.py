class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                output[i] = 1
            else:
                output[i] = output[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output

        
