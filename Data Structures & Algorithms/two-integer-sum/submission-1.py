class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        val_index_pair = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in val_index_pair:
                j = val_index_pair[comp]
                return [i,j] if i < j else [j, i]
            val_index_pair[num] = i 
        return []

        