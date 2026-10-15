from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root)
  
        while True:

            if frontier.is_empty():
                print(f"frontera vacia")
                return NoSolution(reached)
            
            node = frontier.pop()
            print(f"verificando estado {node.state}, costo: {node.cost}")

            if grid.objective_test(node.state):
                print(f"llegada al objetivo")
                return Solution(node, reached)

            for a in grid.actions(node.state):
                print(f"Acciones disponibles: {a}")
                new_state = grid.result(node.state, a)
                new_cost = node.cost + grid.individual_cost(node.state, a)
                
                if new_state not in reached or new_cost < reached[new_state]:
                    new_node = Node("",new_state, new_cost, node, a )
                    reached[new_state] = new_cost
                    frontier.add(new_node)
                    print(f"Agregado a la frontera: {new_node}")
