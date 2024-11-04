import heapq

def a_star(start, goal, grid):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(p):
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            np = (p[0] + dx, p[1] + dy)
            if 0 <= np[0] < len(grid) and 0 <= np[1] < len(grid[0]) and grid[np[0]][np[1]] == 0:
                yield np

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]  # Return reversed path from start to goal

        for next in neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(open_set, (priority, next))
                came_from[next] = current

    return None  # Return None if no path is found
