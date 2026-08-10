class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for i in range(len(nums)):
            current = nums[i]
            other = target - current
            if other in num_index:
                return sorted([i, num_index[other]])
            num_index[current] = i

        