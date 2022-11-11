class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = mat.__len__()
        list_power = [[0, i] for i in range(rows)]

        for i in range(rows):
            for j in range(mat[0].__len__()):
                if mat[i][j]:
                    list_power[i][0] = list_power[i][0] + 1
                else:
                    break

        list_power.sort()

        return [list_power[i][1] for i in range(k)]