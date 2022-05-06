SAT Based Sudoku Pair Solver 

A project to solve sudoku Pair problem (with the constraint S1[i, j] ≠ S2[i, j]) based on Boolean Satisfiability (SAT) solver.

The Sudoku Pair problems are read from the entered csv file

Basially what the program does are:
1. Takes parameter k and single CSV file containing two sudokus as input
2. Reduces Sudoku Pair problem to a SAT clauses
3. Solve the SAT clauses using python SAT Solver (pycosat)
4. Print the Sudoku answer

Usage
python A1_Q1.py 
value of k: <number>
Enter the csv file location: <csv_file_location>


