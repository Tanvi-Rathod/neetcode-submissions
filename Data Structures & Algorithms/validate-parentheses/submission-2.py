class Solution:
    def isValid(self, s: str) -> bool:
        maping_b = {'[':']','(':')','{':'}'}
        stack = []
        for p in s:
            if p in maping_b.keys():
                stack.append(p)
            else:
                if len(stack)==0 or p != maping_b[stack.pop()]:
                    return False

        
        if len(stack) == 0:
            return True
        else:
            return False
            
        