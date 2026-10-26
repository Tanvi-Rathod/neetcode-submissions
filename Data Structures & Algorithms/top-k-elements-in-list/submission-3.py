class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)

        heap = []
        
        for el in count.keys():
            heapq.heappush(heap, (count[el],el) )

            if len(heap) > k:
                heapq.heappop(heap)
        
        final_ans = []
        for i in range(k):
            final_ans.append(heapq.heappop(heap)[1])
        return final_ans
   







        
        