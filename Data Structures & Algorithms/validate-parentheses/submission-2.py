class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'[':']', '{': '}', '(':')'}

        stack = []

        for b in s:
            if len(stack) == 0:
                stack.append(b)
                continue
            
            t = stack.pop()

            if t in brackets.keys():
                if brackets[t] != b:
                    stack.append(t)
                    stack.append(b)
            else:
                stack.append(t)
                stack.append(b)


        return len(stack) == 0
