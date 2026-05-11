class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        ive already been hinted that this is a two pointer approach problem. so i will maintain 2 pointers for the same:

        1. first pointer to keep track of the index of the digits from the front
        2. second pointer to keep track of the index of the digits from the backside

        as long as the indices are not the same, they can be candidates for the target sum.

        and as long as the first index is lower than the second index
        this traversal needs to happen after finding out the length of the list.
        
        this will enable the check to happen in one pass -> O(1) as asked.
        '''

        ptr1 = 1
        ptr2 = len(numbers)

        while ptr1 != ptr2 and ptr1 < ptr2:
            curr = numbers[ptr1 - 1] + numbers[ptr2 - 1]

            if curr == target:
                return [ptr1, ptr2]
            elif curr < target:
                ptr1 += 1
            else:
                ptr2 -= 1