class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        zeroIndex = -1
        product = 1
        for i,num in enumerate(nums):
            if num == 0:
                zeroCount += 1
                zeroIndex = i
                continue
            product = product * num
        
        ans = [0 for x in range(len(nums))]
        if zeroCount > 1:
            return ans
        
        if zeroCount == 1:
            ans[zeroIndex] = product
            return ans
        
        for i,num in enumerate(nums):
            ans[i] = int(product/nums[i])
        
        return ans
                