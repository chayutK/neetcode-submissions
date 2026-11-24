class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers)-1

        while i < j:
            sumint = numbers[i] + numbers[j]
            if sumint < target:
                i += 1
            elif sumint > target:
                j -= 1
            else:
                return [i+1,j+1]
        
        return [i,j]