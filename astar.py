from map import *
from vehicle import *

from collections import *
import copy

Position = namedtuple('Position', 'y x') 
inBoard=[]


#Solver function using A* algorithm
class BoardSolverAStar():
   
    def __init__(self, input):
       
        self.inBoard=input
        self.states=0
        self.et = set()
        self.deq = deque()
        self.win = None
        self.deq.append(Board(input))
        self.et.add(str(self.deq[0]))
 
    def solve(self):
       
        while self.deq:
            self.states+=1
            state = self.deq.popleft()
            
            if state.cars['X'].get_new_pos(1) == state.finish:
                state.moves[-1].direction += 1
                self.win = state
                return
            c_s = state.get_child_states()
            
            for cs in c_s:
                it = str(cs)
                if it not in self.et:
                    self.et.add(it)
                    self.deq.append(cs)
           
        
#Displays the solution 
                    
    def display(self):

        if self.win is None:
            print ("Unsolvable game.")
        else:
            print('\n')
            states=len(self.deq)+2
            newBoard=self.inBoard.split('\n')
            temp=""
            for i in range(6):
                temp+=newBoard[2][i]
            newBoard[2]=temp
            move=0
            for step in self.win.moves:            
                obj=step.obj
                direction=step.direction
                for i in range(abs(direction)):
                    
                    if(newBoard[2][5]=='X' and newBoard[2][4]=='X'): #when the XX car reaches the destination, then the implementation breaks.
                     break
                    move+=1
                    cordx=[]  #x-coordinates
                    cordy=[]  #y-coordinates                 
                  
                    for i in range(6) :
                         for j in range(6):  
                              if newBoard[i][j]==obj[0]:
                                  cordx.append(i)
                                  cordy.append(j)
                             

                    if(cordx[0]==cordx[1]):
                        ans=""
                        if  direction > 0:  
                            for i in range(cordy[0]):
                                ans+=newBoard[cordx[0]][i] 
                             
                            for i in range(1):
                              ans+='-'    
                            
                            for i in range(len(cordx)):
                                ans+=obj[0]
                        
                            index=len(ans)
                            while index<6:
                                ans+=newBoard[cordx[0]][index]
                                index+=1 

                            newBoard[cordx[0]]=ans[0:6]

                        else:
                            
                            for i in range(5,cordy[len(cordy)-1],-1):
                                ans+=newBoard[cordx[0]][i] 
                             
                            for i in range(1):
                              ans+='-'
                            
                            for i in range(len(cordx)):
                                ans+=obj[0]
                            index=6-len(ans)-1
                            while 0<=index:
                                ans+=newBoard[cordx[0]][index]
                                index-=1

                            
                            newBoard[cordx[0]]=ans[::-1]         
                                       
                        for i in newBoard:
                           print(i)  
                        print('\n')        
                    
                    if(cordy[0]==cordy[1]):
                        ans=""
                        tBoard=[]
                        cordx=[]
                        cordy=[]
                        for i in range(6):
                            temp=""
                            for j in range(6):
                                temp+=newBoard[j][i]
                            #print(temp)
                            tBoard.append(temp)

                        for i in range(6) :
                            for j in range(6):
                                if tBoard[i][j]==obj[0]:
                                  #print(i,j)
                                  cordx.append(i)
                                  cordy.append(j)
                        
                        if  direction > 0:  
                            for i in range(cordy[0]):
                                ans+=tBoard[cordx[0]][i] 
                             
                            for i in range(1):
                              ans+='-'    
                            
                            for i in range(len(cordx)):
                                ans+=obj[0]
                        
                            index=len(ans)
                            while index<6:
                                ans+=tBoard[cordx[0]][index]
                                index+=1    
                            tBoard[cordx[0]]=ans

                        else:
                            
                            for i in range(5,cordy[len(cordy)-1],-1):
                                ans+=tBoard[cordx[0]][i] 
                            
                            for i in range(1):
                              ans+='-'
                            
                            for i in range(len(cordx)):
                                ans+=obj[0]
                            index=6-len(ans)-1
                            while index >= 0:
                                ans+=tBoard[cordx[0]][index]
                                index-=1

                            
                            tBoard[cordx[0]]=ans[::-1] 
                        newBoard=[]            
                        for i in range(6):
                            temp=""
                            for j in range(6):
                                temp+=tBoard[j][i]
                            #print(temp)
                            newBoard.append(temp)               
                        #print(newBoard) 
                        for i in newBoard:
                           print(i)

                        print('\n') 

            print("Total Moves: ",move)
         
            print("Total States Explored: "+str(self.states-2))    

    def winner_car_positions_as_dict(self):
      
        end = self.win.cars
        if self.win is None:
            return "Game is unsolvable"
        else:
            for el in end:
               end[el]=(end[el].pos,end[el].size,end[el].is_horizontal)
        return end
                      
    def heuristic0(self):

            ans=0
            index=-1
            for i in self.inBoard[2]:
                if i == 'X':
                    index=i

            for i in range(index,len(self.inBoard[2])):
                if self.inBoard[2][i]!='X' and self.inBoard[2][i]!='-':
                    ans+=1           
           
    def heuristic1 (self):


            moves=len(self.win.moves)
            states=self.states
            
    
    def winner_car_matrix(self):
     
        matrix=[[' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ']]
        pos=self.winner_car_positions_as_dict()
        for car in pos:
            matrix[pos[car][0][0]][pos[car][0][1]]=car
            orientation = pos[car][2]
            size=pos[car][1]
            if orientation==True:
                for i in range(size):
                    matrix[pos[car][0][0]][pos[car][0][1]+i]=car
            else:
                for i in range(size):
                    matrix[pos[car][0][0]+i][pos[car][0][1]]=car
        return matrix


        
