class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        loopCount = 0
        while num>0:
            if num%2==0:
                num = num/2
                loopCount +=1
            else:
                num = num-1
                loopCount +=1

        return loopCount