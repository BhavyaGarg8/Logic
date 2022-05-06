
import pycosat

import random

import csv

def v(n, i, j, d, k):
  # assigning value to each preposition
  return (k**6)*(n-1) + (k**4) * (i - 1) + k**2 * (j - 1) + d



def sudoku_clauses(n ,k):
  res = []

  # cell constraint
  for i in range(1, k*k+1):
    for j in range(1, k*k+1):
      # atleast one number in each cell
      res.append([v(n, i, j, d, k) for d in range(1, k*k+1)])
      for d in range(1, k*k+1):
        for dp in range(d + 1, k*k+1):
          # atmost one number in each cell
          res.append([-v(n, i, j, d, k), -v(n, i, j, dp, k)])

  # row/col constraint
  for i in range (1, k*k+1):
    for j in range(1,k*k +1):
      for jd in range (j+1, k*k +1):
        for d in range (1, k*k +1):
          res.append([-v(n, i, j, d, k),-v(n, i, jd, d, k)]) # row constraint
          res.append([-v(n, j, i, d, k),-v(n, jd, i, d, k)]) # col constraint  

  block_number=[k*i +1 for i in range(k)]

  # block constraint
  for x in block_number:
    for y in block_number:
      temp = [(x + h// k, y + h % k) for h in range(k**2)] # storing the cells of a particular block in temp
      for i in range(k**2):
        for j in range(i+1,k**2):
          for  d in range(1,k**2 + 1):
            # block constraint
            res.append([-v(n, temp[i][0], temp[i][1], d, k),-v(n, temp[j][0], temp[j][1], d, k)])

  return res




def sudoku_pair_clauses(k):
  res = sudoku_clauses(1,k) + sudoku_clauses(2, k)

  # constraint S1[i, j] ≠ S2[i, j]
  for i in range(1,k*k+1):
    for j in range(1,k*k+1):
      for d in range(1,k*k+1):
        res.append([-v(1, i, j, d, k), -v(2, i, j, d, k)])
  
  return res




def sudoku_solver(sudoku , n, k):
  clauses = sudoku_clauses(n, k)

  # adding the already filled numbers in clauses
  for i in range(1, k*k+1):
    for j in range(1, k*k+1):
      d = sudoku[i - 1][j - 1]
      if d:
        clauses.append([v(n, i, j, d, k)])
      
  a = pycosat.solve(clauses)
  sol = list(a)
  if sol == ['U', 'N', 'S', 'A', 'T']:
    return False

  # creating a function which can read sudoku cells through the model
  def read_cell(i, j):
    for d in range(1, k*k+1):
      if v(n, i, j, d, k) in sol:
        return d

  # updating the sudokus
  for i in range(1, k*k+1):
    for j in range(1, k*k+1):
      sudoku[i - 1][j - 1] = read_cell(i, j) 

  return True




def sudoku_pair_solver(sudoku1 , sudoku2, k):
  clauses = sudoku_pair_clauses(k)
  
  # adding the already filled numbers in clauses
  for i in range(1, k*k+1):
    for j in range(1, k*k+1):
      d1 = sudoku1[i - 1][j - 1]
      d2 = sudoku2[i - 1][j - 1]
      if d1:
        clauses.append([v(1, i, j, d1, k)])
      if d2:
         clauses.append([v(2, i, j, d2, k)]) 

  a = pycosat.solve(clauses)
  sol = set(a)

  # creating a function which can read sudoku cells through the model
  def read_cell(n, i, j):
    for d in range(1, k*k+1):
      if v(n, i, j, d, k) in sol:
        return d

  # updating the sudokus
  for i in range(1, k*k+1):
    for j in range(1, k*k+1):
      sudoku1[i - 1][j - 1] = read_cell(1, i, j)
      sudoku2[i - 1][j - 1] = read_cell(2, i, j)




def check_unique(grid1, grid2, k):
  clauses = sudoku_pair_clauses(k)
  
   # adding the already filled numbers in clauses
  for i in range(1, k*k+1):
    for j in range(1, k*k+1):
      d1 = grid1[i - 1][j - 1]
      d2 = grid2[i - 1][j - 1]
      if d1:
        clauses.append([v(1, i, j, d1, k)])
      if d2:
         clauses.append([v(2, i, j, d2, k)]) 

  a = list(pycosat.itersolve(clauses))
  
  # judging the length of a
  if len(a) == 1:
    return True
  else :
    return False




def sudoku1_generator(k, grid1):

  number_list=[i+1 for i in range(k*k)]
  block_number=[k*i +1 for i in range(k)]
  
  # Filling the diagnol blocks of sudoku with random number from (1 to K*k)
  for number in block_number:
    random.shuffle(number_list)
    for i in range(number,number+k):
      for j in range(number,number+k):
        grid1[i-1][j-1]=number_list[(i-number)*k + (j-number)]
  
  # calling sudoku solver to fill the rest of the cells 
  ans = sudoku_solver(grid1, 1, k)

  # if in case sudoku is not generated properly the function is called again
  if ans == False :
    grid1 = sudoku1_generator(k, grid1)
    
  return grid1




def sudoku2_generator(grid1,grid2, k):
  
  # function sudoku_pair_solver in which grid1 is completely filled and grid2 is filled using the func.
  sudoku_pair_solver(grid1, grid2, k)
  
  return grid2




def eraser(grid1,grid2, k):
  cells = []
  
  # all the cells of both sudoku are filled in the list-cells in form of tuple (n,i,j,d)
  for i in range(1, k*k+1):
    for j in range(1, k*k+1):
      a = (1, i, j, grid1[i-1][j-1])
      cells.append(a)
      b = (2, i, j, grid2[i-1][j-1])
      cells.append(b)
  
  # designing a func which can change value in grids
  def ass(n,i,j,d):
    if n==1:
      grid1[i-1][j-1] = d
    else:
      grid2[i-1][j-1] = d

  # erase the cells data one by one until a pair of sudoku with unique solution and maximal holes are left.   
  while len(cells) > 0 :  
    random.shuffle(cells)
    removed_cell = cells.pop(0)
    n = removed_cell[0]
    i = removed_cell[1]
    j = removed_cell[2]
    d = removed_cell[3]
    ass(n,i,j,0)
    
    if check_unique(grid1,grid2, k) == False :
      ass(n,i,j,d)
  
  # checking the pair indeed has unique solution
  # assert check_unique(grid1,grid2, k) == True



# main
k = input("Enter the value of k: ")
k = int(k)
grid1 = [[0 for i in range(k*k)] for j in range(k*k)]
grid2 = [[0 for i in range(k*k)] for j in range(k*k)]

sudoku1_generator(k, grid1)
sudoku2_generator(grid1, grid2, k)

eraser(grid1, grid2, k)

fname = input("Enter the file name to be created: ")
file = open(fname,'w')
csvwriter = csv.writer(file)
for row in grid1:
  csvwriter.writerow(row)
for row in grid2:
  csvwriter.writerow(row)  
file.close()