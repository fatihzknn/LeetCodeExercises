from Counter import Counter
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        counts = Counter(arr)

        unique_elements = [item for item in arr if counts[item] == 1]

        if len(unique_elements) < k:
            return ""
        return unique_elements[k-1]