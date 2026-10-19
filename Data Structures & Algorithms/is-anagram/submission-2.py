class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1
        
        for char in t:
            if char not in count:
                return False
            if count[char] <= 0:
                return False
            count[char] -= 1
        
        for value in count.values():
            if value != 0:
                return False
        return True
            