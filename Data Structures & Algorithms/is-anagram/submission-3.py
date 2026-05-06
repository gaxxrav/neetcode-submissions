class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_list = list(t)
        
        for letter in s:
            if letter in t_list:
                t_list.remove(letter)
            else:
                return False
        
        return True