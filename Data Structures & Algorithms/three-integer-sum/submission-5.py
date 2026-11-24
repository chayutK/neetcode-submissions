class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        i,j,k = 0,1,len(nums)-1
        while i < j and j < k:
            if i != 0 and nums[i-1] == nums[i]:
                i += 1
                j += 1
                continue
            if nums[i] > 0:
                break
            target = -nums[i]
            while j < k:
                if j != i+1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                sums = nums[j]+nums[k]
                if sums < target:
                    j += 1
                elif sums > target:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
            i += 1
            j = i+1
            k = len(nums)-1
        
        return ans


