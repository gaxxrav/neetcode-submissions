class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = defaultdict(int)

        for num in nums:
            h_map[num] += 1

        sorted_hmap = sorted(h_map.items(), key = lambda item: item[1], reverse = True)

        result = []
        for i in range(k):
            result.append(sorted_hmap[i][0])

        return result