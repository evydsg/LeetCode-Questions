class Solution:
    def isValid(self, s: str) -> bool:

        index = 0
        brackets = {')':'(', ']':'[', "}": '{'}
        answer = False
        stack_brackets = []

        for index in range(len(s)):
            if len(stack_brackets) != 0 and (s[index] in brackets) and (brackets[s[index]] == stack_brackets[-1]):
                stack_brackets.pop()
    
            else:
                stack_brackets.append(s[index])
            
        if len(stack_brackets) == 0:
            return True