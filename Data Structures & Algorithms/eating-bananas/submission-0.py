class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_ptr,right_ptr = 1, max(piles)
        


        while left_ptr < right_ptr:
            k = (left_ptr+right_ptr) // 2
            hours_needed = 0

            for pile in piles:
                hours_needed += (pile + k-1) // k

            if hours_needed <= h:
                right_ptr  = k
            else:
                left_ptr = k + 1
        return left_ptr