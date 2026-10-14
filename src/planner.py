import heapq


def heuristic(a, b):
    """Estimate the distance between two grid positions."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(position, width, height, obstacles):
    """Return valid up, down, left, and right neighboring cells."""
    x, y = position

    candidates = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

    return [
        cell
        for cell in candidates
        if 0 <= cell[0] < width
        and 0 <= cell[1] < height
        and cell not in obstacles
    ]


def astar(start, goal, width, height, obstacles=None):
    """Find a shortest path using the A* search algorithm.

    Returns a list of grid positions from start to goal,
    or an empty list if no path exists.
    """
    obstacles = set(obstacles or [])

    if not (
        0 <= start[0] < width
        and 0 <= start[1] < height
        and 0 <= goal[0] < width
        and 0 <= goal[1] < height
    ):
        return []

    if start in obstacles or goal in obstacles:
        return []

    if start == goal:
        return [start]

    frontier = []
    heapq.heappush(frontier, (heuristic(start, goal), start))

    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            path = [current]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            path.reverse()
            return path

        for neighbor in get_neighbors(
            current, width, height, obstacles
        ):
            new_cost = cost_so_far[current] + 1

            if (
                neighbor not in cost_so_far
                or new_cost < cost_so_far[neighbor]
            ):
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)

                heapq.heappush(
                    frontier,
                    (priority, neighbor),
                )
                came_from[neighbor] = current

    return []