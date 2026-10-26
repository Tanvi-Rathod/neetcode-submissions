class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_check = set()
        for element in nums:
            if element in duplicate_check:
                return True
            else:
                duplicate_check.add(element)

        return False
                
        