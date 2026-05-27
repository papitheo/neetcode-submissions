class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for index in range(len(s)):
            # Check the existance of the current element in the dictionary. If it exists,
            # return the value pair and add 1 to it and assign it as the value of that 
            # current element. If it doesn't exist, return 0 and add it to the 1 and 
            # assign it the current element.
           countS[s[index]] = 1 + countS.get(s[index],0)
           countT[t[index]] = 1 + countT.get(t[index],0)
        return countS == countT
        