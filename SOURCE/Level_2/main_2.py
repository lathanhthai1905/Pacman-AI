import handle_input_2 as handlein2
from path_finding_2 import A_star


if __name__ == '__main__':
    level = 'Level_2'
    file_name = 'Map-1.txt'

    maze_size, maze, spawnpoint = handlein2.read_file(level, file_name)

    adjacent_nodes, food = handlein2.handle_adjacent(maze, maze_size)

    # Find food
    path = A_star(maze, adjacent_nodes, spawnpoint, food)

    if path is not None:
        print(path)
    else:
        print("No solution")

    input()
