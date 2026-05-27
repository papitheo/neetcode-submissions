class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to keep the key value pair of the difference and its index
        prevMap = {}
        for index,number in enumerate(nums):
            difference = target - number
            if difference in prevMap:
                return [prevMap[difference],index]
            # add the current to the dic and assign the index as its key
            prevMap[number] = index
        