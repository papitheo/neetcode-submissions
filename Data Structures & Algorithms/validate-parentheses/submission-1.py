class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack=[]

        for ch in s:
            if ch in matches:
                if not stack or stack.pop() != matches[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack