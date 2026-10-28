class Solution:

    def encode(self, strs: List[str]) -> str:
        len_str = ''
        for s in strs:
            len_str+=str(len(s))
            len_str+='#'
            len_str+=s
        return len_str
       


    def decode(self, s: str) -> List[str]:
       
        i = 0
     
        final_list = []
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j= i+length
            final_list.append(s[i:j])
            i=j
  
        return final_list



        




