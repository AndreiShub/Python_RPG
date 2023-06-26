from entities import Player

from map import Maze


def main():
    # player = Player()
    # player.decide_action()

    maze = Maze(5, 5, 2, 2)
    maze.make_maze()
    maze.write_svg('maze.svg')
    print("Начало ", maze.starting_cell.x, maze.starting_cell.y, sep=" ")
    print("Конец ", maze.ending_cell.x, maze.ending_cell.y, sep=" ")
    print(maze)


if __name__ == "__main__":
    main()
