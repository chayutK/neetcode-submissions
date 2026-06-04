class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#"
            encoded += word
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        decoded = []
        while i < len(s):
            numStr = ""
            while s[i] != "#":
                numStr += s[i]
                i += 1
            num = int(numStr)
            start = i+1
            word = s[start:num+start]
            i = num+start
            decoded.append(word)
        return decoded

