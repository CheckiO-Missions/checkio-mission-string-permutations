"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["ab"],
            "answer": ["ab", "ba"]
        },
        {
            "input": ["abc"],
            "answer": ["abc", "acb", "bac", "bca", "cab", "cba"]
        },
        {
            "input": ["a"],
            "answer": ["a"]
        },
        {
            "input": ["abcd"],
            "answer": ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "bacd", "badc", "bcad", "bcda", "bdac", "bdca", "cabd", "cadb", "cbad", "cbda", "cdab", "cdba", "dabc", "dacb", "dbac", "dbca", "dcab", "dcba"]
        },
    ],
    "Extra": [
        {
            "input": ["aab"],
            "answer": ["aab", "aab", "aba", "aba", "baa", "baa"]
        },
        {
            "input": ["aaa"],
            "answer": ["aaa", "aaa", "aaa", "aaa", "aaa", "aaa"]
        },
    ]
}
