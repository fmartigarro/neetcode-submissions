class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         """
         [] -- false
         every elem unique -- true
         Counter
         hashmap
         set
         """

         if not nums:
            False

         seen = {}

         for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True

         return False