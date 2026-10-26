class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            count_map[num] = 1 + count_map.get(num,0)
        
        freq = [[] for i in range(0,len(nums)+1)]
        for key,value in count_map.items():
            freq[value].append(key)

        topk = []
        for li in range(len(freq)-1,-1,-1):
            for i in freq[li]:
                if len(topk)<k:
                    topk.append(i)
                else:
                    break
        return topk

       
   







        
        