class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # maintain a hash map

        hmap = {}

        for element in nums:
            if element not in hmap:
                hmap[element] = 1
            else:
                return True
        
        return False