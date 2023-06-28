from entities import Player

from maze import Maze
from action_handler import decide_action

def main():
    maze = Maze(3,3)
    maze.create()
    maze.populate()

if __name__ == "__main__":
    main()
