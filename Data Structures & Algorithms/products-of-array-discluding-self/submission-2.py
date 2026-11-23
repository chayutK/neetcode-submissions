class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1 for x in range(length)]
        suffix = [1 for x in range(length)]

        for i in range(1,length):
            prefix[i] = prefix[i-1]*nums[i-1]
            suffix[length - i - 1] = suffix[length-i] * nums[length-i]
        
        ans = [1 for x in range(length)]
        for i in range(length):
            if i == 0:
                ans[i] = suffix[i]
            elif i == length-1:
                ans[i] = prefix[i]
            else:
                ans[i] = prefix[i]*suffix[i]
        
        return ans
                