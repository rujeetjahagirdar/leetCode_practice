class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room):
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    dfs(i)
        dfs(0)
        print(visited)
        return len(visited)==len(rooms)