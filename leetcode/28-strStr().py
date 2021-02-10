class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        return haystack.find(needle)