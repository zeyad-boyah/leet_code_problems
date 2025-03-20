import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = re.sub(r'[^a-zA-Z0-9]', '', s)
        filtered_s = filtered_s.lower()
        pointer1 = None
        pointer2 = None
        for i in range(int(len(filtered_s)/2)):
            pointer1 = filtered_s[i]
            pointer2 = filtered_s[-i -1]
            if pointer1 == pointer2:
                continue
            else:
                return False
        return True