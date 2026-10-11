class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # indices i, j -- nums[i] + nums[j] == target. 
        # store value of number we are iterating against -- hashmap - value + index
        # nums[i] = target - nums[j] --> nums[j] = target - nums[i]
        
        index_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement], i]
            
            index_map[num] = i

        # time complexity: O(n) 
        # space complexity: O(n)
        

            
