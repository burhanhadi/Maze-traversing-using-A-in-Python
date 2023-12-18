from updatedPyamaze.pyamaze import maze, agent, textLabel, COLOR
from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

def aStar(m, start, goal):
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0

    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, goal)

    open_set = PriorityQueue()
    open_set.put((h(start, goal), start))

    came_from = {}

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            break

        for d in 'ESNW':
            if m.maze_map[current][d] == True:
                if d == 'E':
                    neighbor = (current[0], current[1] + 1)
                elif d == 'W':
                    neighbor = (current[0], current[1] - 1)
                elif d == 'N':
                    neighbor = (current[0] - 1, current[1])
                elif d == 'S':
                    neighbor = (current[0] + 1, current[1])

                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + h(neighbor, goal)
                    open_set.put((f_score[neighbor], neighbor))

    path = reconstruct_path(came_from, start, goal)
    return path

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

if __name__ == '__main__':
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    start_row, start_col = map(int, input("Enter the start position (row, column): ").split())
    goal_row, goal_col = map(int, input("Enter the goal position (row, column): ").split())

    m = maze(rows, cols, agent_position=(start_row, start_col))
    m.CreateMaze(theme="light")

    start = (start_row, start_col)
    goal = (goal_row, goal_col)

    path = aStar(m, start, goal)

    a = agent(m, goal_row, goal_col, footprints=True, color ="green")
    m.tracePath({a: path})
    
    l = textLabel(m, 'A Star Path Length', len(path) + 1)

    m.run()