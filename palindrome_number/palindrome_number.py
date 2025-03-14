class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  
            return False  
        numbers_list = list(str(x))
        numbers_lists = list(map(int, numbers_list))
        for i in range(int(len(numbers_list)/2)):
            if numbers_list[i] == numbers_list[-i -1]:  
                continue
            else:
                return False
        return True
    

# better solution

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  
            return False  # Negative numbers & numbers ending in 0 (except 0 itself) are not palindromes
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10  # Remove the last digit of x
        
        return x == reversed_half or x == reversed_half // 10  # Even & odd digit cases

"""
