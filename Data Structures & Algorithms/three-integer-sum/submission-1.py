class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        i,j,k = 0,1,len(nums)-1
        while i < j and j < k:
            target = -nums[i]
            while j < k:
                sums = nums[j]+nums[k]
                if sums < target:
                    j += 1
                elif sums > target:
                    k -= 1
                else:
                    ans.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
            i += 1
            j = i+1
            k = len(nums)-1
        
        return [list(i) for i in ans]


