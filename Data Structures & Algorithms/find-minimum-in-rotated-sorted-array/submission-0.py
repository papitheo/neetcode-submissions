class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_idx,right_idx = 0, len(nums) - 1

        while left_idx < right_idx:
            mid_idx = left_idx + (right_idx - left_idx) // 2


            if nums[mid_idx] > nums[right_idx]:
                left_idx  = mid_idx + 1
            else:
                right_idx  = mid_idx

        return nums[left_idx]