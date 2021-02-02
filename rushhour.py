from astar import *
import os
import sys
def rushhour(heuristic,board):
    
    boards=[board[0], board[1],board[2],board[3],board[4],board[5]]

    print(boards[0])
    print(boards[1])
    print(boards[2])
    print(boards[3])
    print(boards[4])
    print(boards[5])

    boards[2]+='>'
    board=boards[0]+'\n'+boards[1]+'\n'+boards[2]+'\n'+boards[3]+'\n'+boards[4]+'\n'+boards[5]+'\n'   
    p = BoardSolverAStar(board)

    p.solve()
    p.display()
    
    if(heuristic == 0):
            p.heuristic0()    
    elif(heuristic == 1):
            p.heuristic1()        

def main():
    cmd=sys.argv[1]
    heno=int(cmd[9])
    temp=""
    for i in range(11,len(cmd)-1):
    	temp+=cmd[i]	
    rushhour(heno,temp)    
  
    
def readf(file):
    with open(file) as f:
        data=f.read()
    return data
