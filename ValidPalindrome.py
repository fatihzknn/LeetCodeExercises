class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()  

        for i in range(0,len(s)):
            if s[i] != s[-i-1]:
                return False
        
        return True