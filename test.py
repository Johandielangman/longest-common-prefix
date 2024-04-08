import unittest
from main import Solution

# Create a list of tests to run
# Each test is a tuple with the first element being a dictionary of input arguments
# and the second element being the expected output
tests = [
    [{"strs": ["flower", "flow", "flight"]}, "fl"],
    [{"strs": ["dog", "racecar", "car"]}, ""],
    [{"strs": ["", ""]}, ""],
]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for test in tests:
            input, expected = test
            with self.subTest(input=input, expected=expected):
                s = Solution()
                self.assertEqual(s.longestCommonPrefix(**input), expected)


if __name__ == "__main__":
    unittest.main()
