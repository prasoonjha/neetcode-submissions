class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        longest_sequence = 0
        for i, num in enumerate(nums):
            if num-1 not in seen:
                #start of a sequence
                curr_seq = 0

                while num in seen:
                    curr_seq +=1
                    num+=1
                longest_sequence = max(longest_sequence, curr_seq )
        return longest_sequence
