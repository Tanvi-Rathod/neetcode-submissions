class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            sorted_dict[sorted_str].append(s)
        
        return list(sorted_dict.values())

        