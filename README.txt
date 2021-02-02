To run the program on the terminal, open the rushhour.py 
and give the command. For example: 

python rushhour.py rushhour(0, ["--B---","--B---","XXB---","--AA--","------","------"])

I have 4 python files: rushhour.py, vehicle.py, map.py and astar.py

rushhour.py contains the main function and where the necessary functions from other files are also called.
vehicle.py contains the class car with few members of the class.
map.py contains the details of the board where valid moves, valid position are checked and new states are created.
astar.py contains A* algorithm, logic behind board implementation and heuristics. 

Also my program correctly runs the hardest rushhour algorithm in 93 moves (as desired).
["MMMDEF",
 "ANNDEF",
 "A-XXEF",
 "PPC---",
 "-BC-QQ",
 "-BRRSS"]