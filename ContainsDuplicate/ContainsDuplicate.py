class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for i in nums:
            if i in hset:
                return True
            else:
                hset.add(i)