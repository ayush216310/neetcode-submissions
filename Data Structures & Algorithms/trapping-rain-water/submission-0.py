class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, 0
        i = 0
        j = len(height)-1
        area = 0
        while i < j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])

            if left_max < right_max:
                area += (left_max - height[i])
                i += 1
            else:
                area += (right_max - height[j])
                j -= 1
        return area