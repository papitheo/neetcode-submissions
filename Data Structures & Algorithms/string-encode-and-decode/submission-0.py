class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for word in strs:
            encodedString += str(len(word)) + "#" + word
        return encodedString


    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            sizeOfWord = int (s[i:j])
            i = j + 1
            j = i + sizeOfWord
            decodedString.append(s[i:j])
            i = j

        return decodedString

