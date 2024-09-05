class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracketList = {"(":")","[":"]","{":"}"}
        for i in s:
            if i != bracketList[i]:
                return False
        return True
        

s = "{}[}"