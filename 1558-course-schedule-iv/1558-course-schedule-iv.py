class Solution:
    # Iterate over each node and perform BFS starting from it.
    # Mark the starting node as a prerequisite to all the nodes in the BFS
    # traversal.
    def preprocess(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        adjList: dict[int, List[int]],
        isPrerequisite: List[List[bool]],
    ) -> None:
        for i in range(numCourses):
            q = deque([i])

            while q:
                node = q.popleft()

                for adj in adjList.get(node, []):
                    # If we have marked i as a prerequisite of adj it implies we
                    # have visited it. This is equivalent to using a visited
                    # array.
                    if not isPrerequisite[i][adj]:
                        isPrerequisite[i][adj] = True
                        q.append(adj)

    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adjList = {}
        for edge in prerequisites:
            if edge[0] not in adjList:
                adjList[edge[0]] = []
            adjList[edge[0]].append(edge[1])

        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        self.preprocess(numCourses, prerequisites, adjList, isPrerequisite)

        answer = []
        for query in queries:
            answer.append(isPrerequisite[query[0]][query[1]])

        return answer