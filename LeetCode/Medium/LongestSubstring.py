# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring(s):
        dicts = {}
        maxlength = start = 0
        for i, value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength


print(lengthOfLongestSubstring("dvdf"))
