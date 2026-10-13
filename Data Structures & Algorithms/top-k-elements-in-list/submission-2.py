import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        # Count the frequency of each number
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        # Return the k most frequent numbers
        return heapq.nlargest(k, seen, key=lambda x: seen[x])