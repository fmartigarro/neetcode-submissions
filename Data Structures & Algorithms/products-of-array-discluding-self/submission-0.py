class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # original method; find multiplicative combo without 0
        # divide each number [i] by that multplicative combo. 

        # two passes: one calculates products, but shifts answers one index up
        # second pass goes reverse order and calculates product, but shifts answers one index back
        # what that leaves is the prefix product plus postfix products except the self product due to offsetting

        products = [1] * len(nums)
        prefix = 1
        postfix = 1

        # [1, 1, 1, 1]

        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]

        return products

