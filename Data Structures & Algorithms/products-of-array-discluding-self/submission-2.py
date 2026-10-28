class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix_mul = n*[1]
        suffix_mul = n*[1]
        p_start = 1
       
        p_start = 1
        s_start = n - 2
        


        for i in range(p_start,n):
            prefix_mul[i] = prefix_mul[i-1]*nums[i-1]
        
        for i in range(s_start,-1,-1):
            suffix_mul[i] = suffix_mul[i+1]*nums[i+1]

        ans_list = []

        for i in range(0,n):
            ans_list.append(prefix_mul[i]*suffix_mul[i])
        
        return ans_list


       