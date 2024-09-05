class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numDict = {}
        for i in nums:
            if i not in numDict.keys():
                numDict[i] = 1
            else:
                numDict[i] +=1
                return True
        
        return False
        




