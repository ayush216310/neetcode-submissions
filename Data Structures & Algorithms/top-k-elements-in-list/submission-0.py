class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        arr = [[] for i in range(len(nums)+1)]
        for key, value in freq_dict.items():
            arr[value].append(key)
        ans = []
        for i in range(len(nums), 0, -1):
            for num in arr[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans
