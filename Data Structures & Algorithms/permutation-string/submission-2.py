class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hi stream
        # its gonna be a silent stream cus im gonna have to get ready to go to work soon. :)
        # https://chatgpt.com/s/t_6a2624fcabf48191b8dd771eca4b393d

        '''
        2 string, s1, s2. True if s2 CONTAINS a permutation of s1. (else False)
        think in terms of SUBSTRING.

        honestly i can just make it a set and check for IN condition.
        whats the diff bw a permutation and a combination?

        this is exactly why i cant check for IN.
        because ORDER MATTERS for permutations

        the constraints are insane. which is why brute force would never even be TRIED.

        imagine having a permutation of 1000 character word. XD

        i get the solution but i need to construct it in my head.


        -----------
        so i start with checking-> if len(s2) > len(s1): return False
        but thats only an edge case.

        now what?
        
        we create 2 pointers to form our window.
        L = s2[0] and R = s2[0]

        ill have a pointer for s1, and 2 pointers for s2.

        move pointer in s2 till i find the first character of s1.

        P = s1[0]
        P1 = s2[0], P2 = P1

        if P1 == P:
            move P2 forward and move P forward.
        '''
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False