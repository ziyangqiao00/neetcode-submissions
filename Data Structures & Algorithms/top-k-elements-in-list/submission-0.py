class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        pairs = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)
        return [num for num, count in pairs[:k]]