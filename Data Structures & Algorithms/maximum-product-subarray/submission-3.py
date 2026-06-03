class Solution:
    """
    first figure out the number of -ves in the array
    if even,
    for each index i, look at what is the current max product subarray
    if a number is negative, take its absolute value

    if odd,
    for example 3 
    state i

    nums[1,2,-3,4]
    for any ith number, the current max and min prod depends 
    only on max[i-1] and min[i-1]
    max[1,2,2,4]
    min[1,1,-6,-24]
    
    """
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_p = [1]*n
        min_p = [1]*n
        
        for i in range(n):
            curr_num = nums[i]
            if i ==0:
                max_p[i] = curr_num
                min_p[i] = curr_num
                continue
            max_p[i] = max(curr_num, curr_num*min_p[i-1], curr_num*max_p[i-1])
            min_p[i] = min(curr_num, curr_num*min_p[i-1], curr_num*max_p[i-1])


        return max(max_p)