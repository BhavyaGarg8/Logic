SAT SOLVER
A Python SAT solver implementation, based on the Semantic tableux method.

This solver is an assignment for the Mathematics For Computer Science II and is meant to provide us with the basics of SAT solving techniques. 

The Problem is read from the entered cnf file.

Basially what the program does are:
1. Takes single cnf file containing the problem in dimacs format.
2. Reduces it into a Link_List of clauses.
3. Solve the Clauses using Solve function and provide a satfiable interpretation if possible.
4. Convert interpretation into model.
5. Print the model if possible or print "UNSAT".

Usage
python A2_Q1.py 
Enter the file location :<csv_file_location>