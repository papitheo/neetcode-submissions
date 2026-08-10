class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_ptr, right_ptr = 0,len(nums) - 1


        while left_ptr <= right_ptr:
            mid_ptr = left_ptr + (right_ptr - left_ptr) // 2
            if target == nums[mid_ptr]:
                return mid_ptr
            elif target > nums[mid_ptr]:
                left_ptr = mid_ptr + 1
            else:
                right_ptr = mid_ptr - 1
        return -1