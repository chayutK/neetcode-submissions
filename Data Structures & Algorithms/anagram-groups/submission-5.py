class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = [0 for x in range(26)]
            start = ord('a')
            for char in word:
                index = ord(char)-start
                count[index] += 1
            countTuple = tuple(count)
            if countTuple not in groups:
                groups[countTuple] = []
            groups[countTuple].append(word)
        
        return [val for val in groups.values()]
