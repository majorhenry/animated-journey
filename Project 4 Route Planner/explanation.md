A* algorithm
A-Star Search algorithm is one of the best and popular technique used in path-finding and graph traversals. Many games and web-based maps use this algorithm to find the shortest path very efficiently. It is often used in video games for each enemy to find a path to the goal (ex. WarCraft).

A* always selects the location with shortest total distance from start to goal ("Best estimated total path cost first"). This is superior to Uniform Cost algorithm which always selects the location with shortest distance from the start location ("Best path cost first"), therefore leading to excessive exploration of the map. On the other hand, Uniform cost is guaranteed to return the shortest path.

A* uses a heuristic function to estimate the distance between two locations. A* is guaranteed to find the solution provided this estimating function returns a distance which is less than or equal to the true path length between the points. Since the 2D coordinates of each locations are provided, I use the euclidian distance, or straight-line distance, between a point and the target. This is guaranteed to be shorter than reality.

As a consequence, A* combines the advantages of a greedy search and the Uniform Cost search which is guaranteed and provides the best search strategy.

A* estimation function f can be broken into: f = g + h where g is the path cost from the start location up to current location and h is the estimated distance from the current location to the goal point.

By minimizing g, the algorithm allows to keep the path as short as possible.
By minimizing h, it allows to stay focused on finding the goal (and reduce unnecessary exploration).
Besides the euclidian distance, 2 other estimators are commonly used:

MANHATTAN DISTANCE: counting the sum of the necessary movements on x and y axis. Used when only vertical and horizontal movements are allowed.

DIAGONAL DISTANCE: This counts the maximum of either the vertical distance on y axis or the horizontal distance on x axis. This guarantees to be optimistic about the true distance (pythagore theorem). This is used when it is allowed to move on all 8 directions of a 2D chessboard (think of the queen in Chess). The Euclidean distance is used when all directions are allowed.

In the worst case, time complexity is O(E), where E is the number of edges in the graph (like roads), since a good heuristic allows A* to prune away many of the nodes that a less efficient (or 'uninformed') search would expand. A* is called 'informed' search because some additional information is also present, which make it easy to reach the goal (the estimation of the distance to the target).

You can read a more detailed A* review [here](https://www.geeksforgeeks.org/a-search-algorithm/).