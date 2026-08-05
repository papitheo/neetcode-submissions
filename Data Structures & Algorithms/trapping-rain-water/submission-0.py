class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_ptr, right_ptr = 0, n - 1
        left_max, right_max = 0, 0
        water = 0

        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                if height[left_ptr] > left_max:
                    left_max = height[left_ptr]
                else:
                    water += left_max - height[left_ptr]
                left_ptr+=1
            else:
                if height[right_ptr] > right_max:
                    right_max = height[right_ptr]

                else:
                    water += right_max - height[right_ptr]
                right_ptr-=1
        return water 
