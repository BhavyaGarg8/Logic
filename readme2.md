SAT Based Sudoku Pair Generator 

A project to generate sudoku Pair problems (with the constraint S1[i, j] ≠ S2[i, j]) with maximum holes and unique solution based on Boolean Satisfiability (SAT) solver.

Basially what the program does are:
1. Takes parameter k as input
2. Generate two filled sudokus with the constraint S1[i, j] ≠ S2[i, j] 
3. Erase the cells data randomly one by one until the solution is unique
4. Take file name as input
5. Create the entered name csv file containing two sudokus 

Usage
python A1_Q2.py 
Enter the value of k: <number>
Enter the file name to be created: <csv_file_name>