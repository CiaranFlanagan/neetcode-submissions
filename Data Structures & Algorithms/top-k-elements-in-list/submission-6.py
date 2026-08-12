class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        sorted_list = (sorted(num_count.items(), key=lambda x: x[1], reverse=True))
        for pair in sorted_list:
            if len(result) < k:
                result.append(pair[0])
        return result
            

        