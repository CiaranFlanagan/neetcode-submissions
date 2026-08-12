class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #intialize counter map
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        #create and fill buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in num_count.items():
            buckets[count].append(num)
        #return results
        results = []
        for arr in reversed(buckets):
            for num in arr:
                if len(results) < k:
                    results.append(num)
        return results


            

        