class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        myList = []
        while (n!=1):
            total = 0

            for i in str(n):
                total +=int(i) **2
            myList.append(total)
            n = total
            if(len(myList)!= len(set(myList))):
                return False
            
        return True