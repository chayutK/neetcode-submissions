class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastNumbers = {}
        for i,num in enumerate(nums):
            sub = target - num
            if sub in pastNumbers:
                return [pastNumbers[sub],i]
            pastNumbers[num] = i
        return [-1,-1]
            