class Solution:
    def isValid(self, s: str) -> bool:
        stacks = []
        brack_map = {')': '(', '}':'{',']':'['}


        for c in s:
            if c in brack_map:
                top = stacks.pop() if stacks else '#'
                if top != brack_map[c]:
                    return False
            else:
                stacks.append(c)

        return not stacks
        