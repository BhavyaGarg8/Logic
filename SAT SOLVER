interpret = [] # global

class node:
  def __init__(self, data):
    self.data = data  
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, data):  # inserting a node in the LL
    newNode = node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode 

  def printLL(self):   # printing the LL
    current = self.head
    while(current):
      print(current.data)
      current = current.next

def add_literal(data):    # adding literal to the interpret if possible else return None
  if (interpret == []) :
    interpret.append(data)
    return data

  for lit in interpret:
    if lit + data ==0:
      return None
  
  interpret.append(data)
  return data

def solve(node):    # recursive function to solve the cnf 
  if node == None :
    return True

  for lit in node.data :
    if add_literal(lit) is None:
      continue
    else :
      if solve(node.next) is False:
        interpret.pop()
        continue
      else :
        return True
  return False 

def search(data):      # searching a literal in the interpret
  for p in interpret:
    if p == data:
      return True

  return False


def int_to_model(v) :   # converting interpret to the model
  model = []

  for i in range(1,v+1) :
    if search(i) is True:
      model.append(i)
    elif search(-i) is True:
      model.append(-i)
    else:
      model.append(i)

  return model      
      

# main
cnf = LinkedList()  # LL for clauses

file_name = input("Enter the file location :") 
file = open(file_name) 
# print(file.readline().strip()
# print(len(file.readline().strip()))
c = 0
v = 0
line = file.readline().strip()
while True :
  if line.startswith('c') :
    line = file.readline().strip()
    continue
  if line.startswith('p') :
    words = line.split()
    v = int(words[2])
    c = int(words[3])
    break
# print(s.variables)

while c >0 :
  line = file.readline().strip()
  words = line.split()
  clause = [int(word) for word in words]
  clause.pop()

  cnf.insert(clause)

  c = c-1

file.close()

ans = solve(cnf.head)

if ans is True:
  model = int_to_model(v)
  print(model)
else:
  print("UNSAT")  

# print(interpret)C:\sat solver\Assignment 2\abc.cnf

