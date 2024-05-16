class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {course: set() for course in range(numCourses)}

        for p in prerequisites:
            course = p[0]
            prereq = p[1]
            prereqs[course].add(prereq)

        print(f"prereqs: {prereqs}")

        def search(course):
            # print(f"\tcourse: {course}")
            # print(f"\tvisited: {visited}")
            # print(f"\tprereqs: {prereqs}")
            if course in visited:
                # print("\tcourse in visited, returning false")
                return False
            visited.add(course)

            toremove = set()
            for prereq in prereqs[course]:
                if not search(prereq):
                    return False
                toremove.add(prereq)
            for el in toremove:
                prereqs[course].remove(el)

            visited.remove(course)
            return len(prereqs[course]) == 0
        
        visited = set()
        for course in prereqs:
            # print("toplevel")
            if not search(course):
                return False

        return True
    
