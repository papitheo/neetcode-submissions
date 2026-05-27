class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap to count the occurances of each num in nums
        count = {}
        # create empty lists of length nums. 1 is added because 
        # we are operating in zero based index
        freq = [[] for i in range(len(nums)+1)]

        # count the occurances of each num in nums. If found, increament 
        # the count by 1 else, initialize the count to 1
        for num in nums:
            count[num] = 1 + count.get(num,0)
            # unpack the key-value pair in the count
            # for evevry value in the count, append its key to the freq bucket
            # for a list : [1,1,1,2,2,2,3,3,3,3]
            # count becomes : [1:3,2:3,3:4]
            # freq [0:[],1:[],2:[],3:[1,2],4:[3]]
            # from the code above, no number appears 0 times, no number appear 1 time,
            # no number appears 2 times, 1 and 2 appear 3 times, 3 appears 4 times 
        for key, value in count.items():
            freq[value].append(key)

        result = []
        # iterate from the back of the list to index 0, increameanting by -1
        for i in range(len(freq) - 1, 0, -1):
            # for every sub list in freq, begining from the end
            for n in freq[i]:
                # grab the value in the list, and append it to the res list
                result.append(n)
                # stop append and return the res if the iteration go k times
                if len(result) == k:
                    return result
        
        