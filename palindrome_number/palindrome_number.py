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
