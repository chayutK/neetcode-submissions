class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i <= j:
            if s[i] == "" or s[i].isalnum() != True: 
                i += 1
                continue
            
            if s[j] == "" or s[j].isalnum() != True:
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        return True