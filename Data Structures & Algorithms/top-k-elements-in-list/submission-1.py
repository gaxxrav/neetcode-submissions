class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        create a freq map
        sort the map by value
        return top k elements of the sort
        '''

        fmap = {}

        for num in nums:
            if num not in fmap:
                fmap[num] = 1
            else:
                fmap[num] += 1
        

        sorted_fmap = dict(sorted(fmap.items(), key = lambda x: x[1]))

        print(sorted_fmap)

        return list(sorted_fmap)[-k:]