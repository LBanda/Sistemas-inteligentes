class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __str__(self):
        return f"State: {self.state} Action: {self.action}\n"
    
class Environment:
    def __init__(self, maze):
        self.walls = maze[0]
        self.start = maze[1]
        self.goal = maze[2]

    def print(self):
        for rows in self.walls:
            print(rows)

class SearchAgent:
    def __init__(self, environment):
        self.frontier = [Node(state=environment.start)]
        self.explored = set()
        self.goal_state = environment.goal

    def print_frontier(self):
        print("Frontier:")
        print("----------")
        for node in self.frontier:
            print(node)

    def print_explored(self):
        print("Explored:")
        print("----------")
        for node in self.explored:
            print(node)

    def is_frontier_empty(self):
        return len(self.frontier) == 0

    def is_goal(self, node):
        if node.state == self.goal_state:
            self.solution = []
            while node.parent is not None:
                self.solution.append(node)
                print(f"{node.state}({node.action})")
                node = node.parent
            raise Exception("Solution Found!!!")

    def add_to_frontier(self, node):
        self.frontier.add(node)

    def add_to_explored(self, node):
        self.explored.add(node)

    def is_state_in_frontier(self,node):
        return any(frontier_node.state == node.state for frontier_node in self.frontier)
    
    def is_state_in_explored(self,node):
        return any(explored_node.state == node.state for explored_node in self.explored)

    def actions(self, node):
        pass

    def remove_node(self):
        pass

    def result(self, node):
        pass

    def expand_node(self, node):
        for child in self.result(node):
            if not self.is_state_in_frontier(child) and not self.is_state_in_explored(child):
                self.add_to_frontier(child)
    
    def solve(self):
        while not self.is_frontier_empty():
            try:
                node = self.remove_node()
            except:
                print("Solution not Found!!!")
            try:
                self.is_goal(node)
            except:
                return self.solution
            self.add_to_explored(node)
            self.expand_node(node)


class AgentDepthFirst(SearchAgent):
    def remove_node(self):
        return self.frontier.pop()
    
class MazeSearch(AgentDepthFirst):
    def __init__(self, environment):
        super().__init__(environment)
        self.walls = environment.walls

    def actions(self, node):
        row, col = node.state
        possible_actions = [
            ("up", (row-1, col)),
            ("down", (row+1,col)),
            ("left", (row, col-1)),
            ("right", (row, col+1))
        ]
        return possible_actions
    
    def result(self, node):
        children = []
        height = len(self.walls)
        width = len(self.walls[0])

        for action, (r,c) in self.actions(node):
            if 0 <= r < height and 0 <= c < width and not self.walls[r][c]:
                children.append(Node(state=(r,c),parent=node,action=action))

        return children
    
class MazeSearchBFS(MazeSearch):
    def remove_node(self):
        return self.frontier.pop(0)


maze = ([
    [1,1,0,0,0,0,1],
    [1,1,0,0,0,0,1],
    [1,1,0,0,0,0,1],
    [1,1,0,0,0,0,1],
    [1,1,0,0,0,0,1],
    [1,1,0,0,0,0,1]],
    (5,0),
    (1,2))

maze_environment = Environment(maze)

maze_environment.print()

maze_solve = MazeSearchBFS(maze_environment)
maze_solve.print_frontier()
solution_nodes = maze_solve.solve()
maze_environment.print()