class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for c in ransomNote:
            if c not in magazine:
                return False
            magazine = magazine.replace(c, '', 1)
        return True