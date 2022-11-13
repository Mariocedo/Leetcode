class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDic = dict()
        magazineDic = dict()

        for i in ransomNote:
            ransomNoteDic[i] = ransomNoteDic.get(i, 0) + 1

        for i in magazine:
            magazineDic[i] = magazineDic.get(i, 0) + 1

        for i in ransomNoteDic.keys():
            if magazineDic.get(i, 0) < ransomNoteDic.get(i, 0):
                return False

        return True