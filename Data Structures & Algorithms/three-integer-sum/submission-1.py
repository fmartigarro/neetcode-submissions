class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sorting the nums array
        # having three pointers iterate, need to fix one. will start at 
        # middle iterates until it touches the left or the right, if s

        left = 0
        right = len(nums)-1
        
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                combo = nums[i] + nums[left] + nums[right]
                if combo == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif combo < 0:
                    left += 1
                else:
                    right -= 1
        
        return result