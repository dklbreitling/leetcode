class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def is_pacific_edge(r, c):
            return r == 0 or c == 0

        def is_atlantic_edge(r, c):
            return r == n_rows - 1 or c == n_cols - 1

        def neighbors(r, c):
            l = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            return [(r,c) for r,c in l if r>=0 and c>=0 and r<n_rows and c<n_cols]

        def can_reach(r, c, r_nei, c_nei):  # can neighbor reach cell?
            return heights[r][c] <= heights[r_nei][c_nei]

        def check(r, c, ocean): 
            if (r, c) in ocean:
                return
            ocean.add((r, c))
            for r_nei, c_nei in neighbors(r, c):
                if can_reach(r, c, r_nei, c_nei):
                    check(r_nei, c_nei, ocean)

        n_rows = len(heights)
        n_cols = len(heights[0])

        pac, atl = set(), set()
        for r in range(n_rows):
            for c in range(n_cols):
                if is_atlantic_edge(r, c):
                    check(r, c, atl)
                if is_pacific_edge(r, c):
                    check(r, c, pac)

        both = atl.intersection(pac)
        return [[r, c] for r, c in both]
