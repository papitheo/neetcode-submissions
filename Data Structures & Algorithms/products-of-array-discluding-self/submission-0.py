class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # output[i] becomes the product of elements to the left of i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Multiply by the product of elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output