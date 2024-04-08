from typing import List


class Solution:
    def reset_coll(self):
        self.coll = {
            "a": [],
            "b": [],
            "c": [],
            "d": [],
            "e": [],
            "f": [],
            "g": [],
            "h": [],
            "i": [],
            "j": [],
            "k": [],
            "l": [],
            "m": [],
            "n": [],
            "o": [],
            "p": [],
            "q": [],
            "r": [],
            "s": [],
            "t": [],
            "u": [],
            "v": [],
            "w": [],
            "x": [],
            "y": [],
            "z": [],
            "": []
        }

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        n_list = len(strs)

        if n_list <= 1:
            return strs[0]

        while True:
            strs.sort()
            self.reset_coll()
            for string in strs:
                first_letter = string[0] if string else ""
                self.coll[first_letter].append(string)

            self.flip_coll()
            common_first_letter_cnt = max(list(self.coll.keys()))
            if common_first_letter_cnt != n_list:
                return prefix
            most_letters = self.coll[common_first_letter_cnt]
            prefix += most_letters
            strs = [string[0 + 1:] for string in strs if string and string[0] == most_letters]

            if not strs:
                return prefix

    def flip_coll(self):
        self.coll = {len(val): key for key, val in self.coll.items() if val}


if __name__ == "__main__":
    s = Solution()
    s.longestCommonPrefix(["", ""])
