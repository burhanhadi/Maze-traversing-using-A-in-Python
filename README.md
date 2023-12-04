# Maze-traversing-using-A-in-Python

Project Overview:

In this project, we harnessed the power of the Python pyamaze library, meticulously customized to meet our specific requirements, all within the welcoming environment of Visual Studio Code (VSCode). Our mission? To craft and traverse virtual mazes dynamically generated based on user input. With real-time visualization, the A* search algorithm takes center stage, guaranteeing an optimal solution through the intricate mazes. The marriage of pyamaze and VSCode delivers an interactive and visually captivating experience, showcasing the library's adaptability in the exploration of artificial intelligence and maze-solving algorithms.

Implementation Details:

Overview:
Our Python script leverages the pyamaze library to generate and solve mazes using the A* search algorithm. With user-defined maze dimensions and customized start and goal positions, the script adds a unique touch to an 8x8 maze, tailoring the experience based on the enrollment number ending in '008.'

Algorithm Implementation:
The A* algorithm, a star player in the script, employs the Manhattan distance heuristic function to estimate the cost from the current cell to the goal. Keeping track of 'g_score' and 'f_score,' it efficiently navigates through the maze, ensuring an optimal path is found.

Enhancements to Pyamaze:
Recognizing limitations in the original pyamaze library, where the start and goal positions were fixed, we took matters into our own hands. We enhanced the 'agent' class by updating the 'init' function to include custom starting and goal coordinates. These changes allow for a more accurate and personalized visualization of the maze, providing a clearer understanding of the start and end points.

Visualization:

Agent and Path Tracing:
An agent takes center stage, starting at the goal position. The 'tracePath' method visually outlines the path discovered by the A* algorithm, guiding the agent from the start to the goal in a mesmerizing visual journey.

Path Length Label:
For added clarity, a label showcasing the length of the path, measured in the number of steps, graces the maze visualization. This addition enhances the user experience by providing immediate insight into the complexity of the traversed path.

This project is a testament to the seamless integration of the pyamaze library with the capabilities of Visual Studio Code, offering an engaging and educational exploration of artificial intelligence within the fascinating world of maze-solving algorithms.
