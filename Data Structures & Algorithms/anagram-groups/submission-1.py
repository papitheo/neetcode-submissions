class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for character in word:
                # gives the actual position of the character in alphabetical order
                # so if you have "cat" and "tac", from "cat", it will put '3' at 3,
                # 'a' at 1, 't' at 20. For "tac", 't' will be put 20, a at 1 and c at 3
                count[ord(character) - ord('a')] += 1
            # after each word is processed, the character positions will be the key
            # so if the key is looked for in ans, and found, it appends the word to 
            # the list, else a new dict is created with that key
            # because count is a list and cannot be used as dictionary key because 
            # it is mutable but keys used in dict are not suppose to be mutable, we 
            # wrap the count with tuple which is immutable so it would work.
            # using the tuples also allows us to use the count list as a single composite key
            ans[tuple(count)].append(word)
        return ans.values()
            
        