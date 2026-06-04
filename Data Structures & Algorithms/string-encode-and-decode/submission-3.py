class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(str(len(word)))
            encoded.append("#")
            encoded.append(word)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            pos = i
            while s[pos] != "#":
                pos += 1
            num = int(s[i:pos])
            start = pos+1
            word = s[start:num+start]
            i = num+start
            decoded.append(word)
        return decoded

