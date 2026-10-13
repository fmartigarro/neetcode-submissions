class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        # ---- worst case solution

        return sorted(seen, key=lambda x: seen[x], reverse=True)[:k]
        
        

        
        