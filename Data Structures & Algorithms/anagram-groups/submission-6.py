class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            sortedStr = "".join(sorted(s))
            group[sortedStr].append(s)   

        return list(group.values())