class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_value = {}
        for i,n in enumerate(nums):
            index_value[n] = i
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in index_value and index_value[diff] != i:
                return [i,index_value[diff]]
            
        return []



        