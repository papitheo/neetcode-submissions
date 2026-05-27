class Solution:

    def encode(self, strs: List[str]) -> str:
        # Declare an empty String to store the encoded string
        encodedString = ""
        
        # loop through the list of string, retrieving each string 
        # and encoding it 
        for word in strs:
            # append the length of the word to a pound sign to separate the 
            # string being read from the length of the that same string
            encodedString += str(len(word)) + "#" + word
        # return the encoded string
        return encodedString


    def decode(self, s: str) -> List[str]:
        # declare an empty list to store the 
        decodedString = []
        # declare and initialize an index to keep tack of the 
        # start of a new word to read
        i = 0

        # Loop through the entire encoded string till the end
        while i < len(s):
            # j would be the pointer moving throught the string while i moves once 
            j = i
            # loop through the ended list until a pound sign '#'
            while s[j] != '#':
                j += 1
            # Store the length of the word read into sizeOfWord 
            # we are casting into int because the length of thw 
            # word is part of the encoded string
            sizeOfWord = int (s[i:j])
            # jump to the first character in the encoded string and assign the index to i
            i = j + 1
            # assign the size of the length of the word to j
            j = i + sizeOfWord
            # retrieve the word from i to j exclusive and append it to the decoded string list
            decodedString.append(s[i:j])
            # assign the size of the index of the last char in the retrieved word to i 
            i = j

        return decodedString

