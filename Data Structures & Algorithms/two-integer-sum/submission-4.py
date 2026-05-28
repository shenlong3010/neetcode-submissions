class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = defaultdict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in mapping:
                return [mapping[complement], i]
            mapping[num] = i
        return []