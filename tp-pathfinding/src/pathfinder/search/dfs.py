from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        node = root
        frontier = StackFrontier()
        frontier.add(node)

        while True:

            if frontier.is_empty():
                return NoSolution(expanded)
            
            node = frontier.remove()
            if node.state in expanded:
                continue
            expanded[node.state] = True
            for a in grid.actions(node.state):
                new_state = grid.result(node.state, a)
                if new_state not in expanded:
                    new_node = Node("",new_state, node.cost + grid.individual_cost(node.state,a), node, a)
                    if grid.objective_test(new_state):
                        return Solution(new_node, expanded)
                    expanded
                    frontier.add(new_node)
