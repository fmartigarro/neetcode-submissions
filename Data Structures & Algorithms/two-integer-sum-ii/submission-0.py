class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array is increasing. need two numbers that add up to target.

        left = 0
        right = len(numbers) - 1

        while left < right:
            combo = numbers[left] + numbers[right]
            if combo == target:
                return [left+1, right+1]
            
            if combo < target:
                left += 1
            elif combo > target:
                right -= 1
        
        return -1
            