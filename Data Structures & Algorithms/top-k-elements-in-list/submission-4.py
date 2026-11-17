class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        maxCount = 0
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
            if counts[num] > maxCount:
                maxCount = counts[num]
        
        kNums = {}
        for key,val in counts.items():
            if val not in kNums:
                kNums[val] = []
            kNums[val].append(key)
        
        ans = []
        for i in range(maxCount):
            index = maxCount - i
            if index not in kNums:
                continue
            for num in kNums[index]:
                ans.append(num)
            if len(ans) >= k:
                break
        return ans[:k]

            

        