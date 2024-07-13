from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        st1, st2 = Counter(ransomNote), Counter(magazine)
        return st1 & st2 == st1

        

a = Solution()
print(a.canConstruct("aa","abb"))