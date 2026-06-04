class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNum = {}
        maxCount = 0
        
        for num in nums:
            if num not in countNum:
                countNum[num] = 0
            countNum[num] += 1
            if maxCount < countNum[num]:
                maxCount = countNum[num]
        
        topK = []
        print(maxCount)
        reversedCount = {}
        for num in countNum.keys():
            count = countNum[num]
            if count not in reversedCount:
                reversedCount[count] = []
            reversedCount[count].append(num)
            
        print(reversedCount)
        i = maxCount
        while i >= 0 and len(topK) < k:
            if i in reversedCount:
                for num in reversedCount[i]:
                    topK.append(num)
            i -= 1
        return topK[:k]