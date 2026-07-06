class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded
    def decode(self, s: str) -> List[str]:
        strs = []
        curr = ""
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            l = int(s[i:j])
            word = s[j+1 : j+1+l]
            strs.append(word)
            i = j + 1 + l
        return strs

            