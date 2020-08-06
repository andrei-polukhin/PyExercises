"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

from typing import List


class Solution:
    def __init__(self, string: str):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __str__(self):
        return f"\"{self.string}\""

    def main(self) -> int:
        if not self.string:
            return 0
        container = self.all_substrings()
        for substring in container:
            if len(set(substring)) == len(substring):
                return len(substring)

    def all_substrings(self) -> List:
        substrings = []
        for length in range(1, len(self.string)+1):
            str_of_spec_length = [
                self.string[i:i+length]
                for i in range(len(self.string)-length+1)
            ]
            substrings.extend(str_of_spec_length)
        return substrings[::-1]


if __name__ == "__main__":
    list_of_strings = [
        "dvdf", "", "abdcdeg", "abcc", "bcsa", "asdgsdte", "  "
    ]
    for string in list_of_strings:
        obj = Solution(string)
        print(str(obj), " => ", obj.main())
