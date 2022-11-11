class Solution:
    def romanToInt(self, s: str) -> int:

        comb = [["_", "_", "M", 1000],
                ["M", "D", "C", 100],
                ["C", "L", "X", 10],
                ["X", "V", "I", 1]
                ]

        number = 0

        for block in comb:
            elem10 = block[0]
            elem5 = block[1]
            elem1 = block[2]
            basis = block[3]

            if s.startswith(elem1 + elem10):
                number = number + basis * 9
                s = s[2:]

            elif s.startswith(elem1 + elem5):
                number = number + basis * 4
                s = s[2:]

            elif s.startswith(elem5):
                number = number + basis * 5
                s = s[1:]

            i = 0
            while i < s.__len__() and s[i] == elem1:
                number = number + basis
                i = i + 1

            s = s[i:]

        return number

