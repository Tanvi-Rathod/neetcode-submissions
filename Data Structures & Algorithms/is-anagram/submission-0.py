class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_frequency = {}
        for char in s:
            if char in char_frequency:
                char_frequency[char]+=1
            else:
                char_frequency[char] = 1

        
        for char in t:
            if char in char_frequency:   
                char_frequency[char]-=1
                if char_frequency[char] == 0:
                    char_frequency.pop(char)
                 
            else:
                return False
        
        if len(char_frequency) == 0:
            return True
        
        return False
        
        