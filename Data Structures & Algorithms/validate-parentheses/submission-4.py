class Solution:
    def isValid(self, s: str) -> bool:
        maping_b = {'[':']','(':')','{':'}'}
        stack = []
        for p in s:
            if p in maping_b.keys():
                stack.append(p)
            else:
                if not stack or p != maping_b[stack.pop()]:
                    return False
        
        return True if not stack else False

        

            
        