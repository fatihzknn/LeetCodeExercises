class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        hash_map = {}
        set_used = set()

        for s_char, t_char in zip(s, t):
            if s_char in hash_map:
                if hash_map[s_char] != t_char:
                    return False
            else:
                if t_char in set_used:
                    return False
                hash_map[s_char] = t_char
                set_used.add(t_char)

        return True