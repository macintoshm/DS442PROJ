# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def makeSearchTree(problem):
    pos = problem.getStartState()
    tree = [pos]
    tier = 0

    while(): 
        tier += 1
        sucessors = problem.getLegalActions(pos)
        for nextPos in sucessors:
            if nextPos == pos:
                continue
            else:
                continue
    #for x in getsucessors
    #if it's already in the above tier, then don't add it
    #if getSucessors is empty after not adding it,break
    # if it's not already in the above tier, add it 
    

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    import pacman
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    location = problem.getStartState()
    dirStack = util.Stack()
    locStack = util.Stack()
    locStack.push(location)
    stackSize = 1
    visitedLocations = [location]

    completed = False
    while not problem.isGoalState(location): #check if existing location is goal state
        print("location: " + str(location))
        print("visitedLocations: " + str(visitedLocations))
        nextLocations = problem.getSuccessors(location) #get list of successor locations for current state
        print("nextLocations: " + str(nextLocations))
        for j in nextLocations: #loop through each possible successor location (end on a state on previously visited)
            for i in visitedLocations: #loop through previously listed locations to check a match
                previouslyListed = False
                if(i == j[0]): #match identified
                    previouslyListed = True
                    break
            print("nextLocations2: " + str(nextLocations))
            print("previouslyListed: " + str(previouslyListed))
            if (not previouslyListed):
                visitedLocations.append(j[0]) #add currently viewed location to visted array
                print("pushed: " + j[1])
                dirStack.push(j[1])
                locStack.push(j[0])
                stackSize += 1
                location = j[0]
                break
        #if all of these locations were visited
        if previouslyListed and not dirStack.isEmpty():
            temp = dirStack.pop()
            print("popped: " + str(temp))
            location = locStack.pop() #set the while loop location to the previous node
            stackSize -= 1

    ans = []
    while(not dirStack.isEmpty()):
        temp = dirStack.pop()
        if(stackSize > 1):
            ans.append(temp)
        print(ans)

    ans.reverse()
    print("ans: " + str(ans))
    return ans 

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
