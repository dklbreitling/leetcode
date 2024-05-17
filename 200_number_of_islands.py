class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        seen = set()
        count = 0

        def neighbors(r, c):
            l = [(r+1,c), (r-1,c), (r,c+1) , (r,c-1)]
            return [(ro, co) for ro, co in l if ro < num_rows and ro >= 0 
                                                and co < num_cols and co >= 0]

        def search(r, c):
            print(f"searching {r, c}")
            if (r, c) in seen:
                return
            if grid[r][c] == "1":
                seen.add((r, c))
                for r_nei, c_nei in neighbors(r, c):
                    if grid[r_nei][c_nei] == "1":
                        search(r_nei, c_nei)

        print(f"seen is {seen}")
        for r in range(num_rows):
            for c in range(num_cols):
                if (r, c) not in seen:
                    print(f"at {r, c}, grid[r][c] {grid[r][c]}")
                    if grid[r][c] == "1":
                        count += 1
                        search(r, c)

        return count

