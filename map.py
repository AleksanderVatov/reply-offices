from pathfinding.core.grid import Grid, Node
from pathfinding.finder.a_star import AStarFinder

from typing import Tuple, List, Union, TextIO

costs =  {
    '#': 0,
    '~': 800,
    '*': 200,
    '+': 150,
    'X': 120,
    '_': 100,
    'H': 70,
    'T': 50
}

class Map:
    """
    Represents a world map.

    Attributes:
        customers(List[Map.Customer]): The customers in the world map
        grid(pathfinding.core.grid.Grid): the underlying grid
        finder(pathfinding.finder.a_star.AStarFinder): the A* finder used to find paths

    """
    def __init__(self, source: Union[str, TextIO]):
        """
        Reads a new map from a file or a string
        :param source: the file-like object or string describing the map (not a filename!)
        """
        if isinstance(source, str):
            input_string = source
        else:
            input_string = source.read()
        lines = input_string.splitlines()
        width, height, nCustomers, self.replyOffices = tuple(map(int,lines[0].split(' ')))
        self.customers = []
        for line in lines[1:1 + nCustomers]:
            x, y, reward = map(int,line.split(' '))
            self.customers.append(Map.Customer((x,y),reward))
        cost_matrix = []
        for line in lines[nCustomers + 1:] :
            cost_matrix.append([costs[char] for char in line])

        self.grid = Grid(width, height, cost_matrix)
        self.finder = AStarFinder()

    def path(self, start:Tuple[int,int], end:Tuple[int,int]) -> 'Map.Path':
        """
        Finds the cheapest path between start and end.
        :param start: The start node, represented as an (x, y) tuple
        :param end: The end node, represented as an (x, y) tuple
        :return Map.Path: The path
        """
        nodes = self.finder.find_path(self.grid.node(*start),self.grid.node(*end),self.grid)[0]
        return Map.Path(nodes, self.grid)


    class Path:
        """
        A path between two nodes in a particular map

        Attributes:
            nodes (List[Tuple[int,int]): A list of all points, including the start and end points
            grid (pathfinding.core.grid.Grid) The grid of the map
        """
        def __init__(self, nodes: List[Tuple[int,int]], grid: Grid):
            self.nodes = nodes
            self.grid = grid

        def __str__(self):
            """
            Converts the path to a string in the format specified by the challenge
            """
            s = ''
            for i in range(len(self.nodes)-1):
                x, y = self.nodes[i]
                x_next, y_next = self.nodes[i + 1]
                if x_next == x + 1:
                    s += 'R'
                elif x_next == x - 1:
                    s += 'L'
                elif y_next == y + 1:
                    s += 'D'
                elif y_next == y - 1:
                    s += 'U'

            return s

        def cost(self) -> int:
            """
            Calculates the cost of the path, or -1 if no path exists
            :return: The cost of the path as an int
            """
            if len(self.nodes) == 0:
                return -1
            else:
                return sum((self.grid.node(x,y).weight for x, y in self.nodes[1:]))

    class Customer:
        """
        Represents a customer.

        Attributes:
            location (Tuple[int,int]): the location of the customer's headquarters
            reward (int): the reward associated with this customer
        """
        def __init__(self, location, reward):
            self.location, self. reward = location, reward