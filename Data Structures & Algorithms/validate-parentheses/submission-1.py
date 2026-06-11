class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        brack_dict = {'}': '{', ']': '[', ')': '('}
        closing = [')', ']', '}']
        opening = ['(', '[', '{']

        for bracket in s:
            if bracket in opening:
                mystack.append(bracket)
            else:
                if bracket in closing and mystack and mystack[-1] == brack_dict[bracket]:
                    mystack.pop()
                else:
                    return False

        return mystack == []