class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            len_longest = -1
            we can update the global longest pointer at each iteration
            if we update the pointers at each iteration, we could do this in O(n) time
            and space.
            we need to keep a track of the numbers where a sequence  might start
            then in respective entries, we keep storing the sequence
            so num in nums, if num-1 not in array, start of a consequtive sequence
            in dict
            how to track a seq? a num-1 in array, this means that this number is part of 
            an already existing subsequence
            sequences[num] = set().add()
        """
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # only start counting if num is the start of a sequence
            if num - 1 not in num_set:
                curr = num
                length = 1

                while curr + 1 in num_set:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest