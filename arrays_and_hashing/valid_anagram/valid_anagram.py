class SolutionOne:
    def isAnagram(self, s: str, t: str) -> bool:
        # make a dict with the first string that contains every letter and it's number of occurance 
        # then iterate over the other string and deduct the number of letters if they exist in the first string 
        dict_of_s = {}
        if len(s) != len(t): return False
        for letter in s:
            if letter in dict_of_s.keys():
                dict_of_s[letter] = dict_of_s[letter] + 1
            else: dict_of_s[letter] = 1
        for letter in t:
            if letter in dict_of_s.keys() and dict_of_s[letter] != 0 :
                dict_of_s[letter] = dict_of_s[letter] - 1
            else: return False

        return True

class SolutionTwo:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashed_s = [0] * 26  # from a-z
        hashed_t = [0] * 26
        for L in range(len(s)):
            hashed_s[ord(s[L]) - ord("a")] += 1
            hashed_t[ord(t[L]) - ord("a")] += 1

        return hashed_s == hashed_t
