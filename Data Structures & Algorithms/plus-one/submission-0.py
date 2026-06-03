class Solution:
   
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        loop_complete = False
        for i in range(n-1, -1, -1):
            curr = digits[i]
            if curr< 9:
                digits[i] = curr+1
                return digits
            else:
                digits[i] = 0
                loop_complete = True
        
        else:
            return [1]+digits