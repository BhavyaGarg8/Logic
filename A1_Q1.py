
import pycosat
import csv



def v(n, i, j, d, k):
  # assigning value to each preposition
  # n represents sudoku number(1,2)
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


# block conatraint
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
  model = list(a)

  if model == ['U', 'N', 'S', 'A', 'T']:
    return False

  # creating a function which can read sudoku cells through the model
  def read(n, i, j):
    for d in range(1, k*k+1):
      if v(n, i, j, d, k) in model:
        return d

  # updating the sudokus            
  for i in range(1, k*k+1):
    for j in range(1, k*k+1):
      sudoku1[i - 1][j - 1] = read(1, i, j)
      sudoku2[i - 1][j - 1] = read(2, i, j)
  
  return True


# main 
k = input("value of k: ")
k = int(k)

sudoku1 = []
sudoku2 = []

try:
  fname = input("Enter the csv file location: ")
except:
  print("File not Found!!") 
  exit() 
  
file = open(fname)
csvreader = csv.reader(file)
tt = 1
for row in csvreader:
  if tt <= (k**2):
    sudoku1.append([int(d) for d in row])
  else :
    sudoku2.append([int(d) for d in row])
  tt = tt + 1        
file.close() 

ans = sudoku_pair_solver(sudoku1, sudoku2, k)

if ans :
  for rows in sudoku1:
    print(rows)
  print("\n")
  for rows in sudoku2:
    print(rows) 
else:
  print("None")