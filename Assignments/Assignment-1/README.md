# Title: Design, Analysis and Validation of an Efficient Search Strategy for a Student Record System

**Objective:** To design, analyse and compare algorithms for searching a student record by registration number as the database grows from 1,000 to 1,000,000 records.

**Software Used:** Python 3.13

**Tools:** VS Code, matplotlib

**Algorithms:**
1. Linear Search (iterative, brute force)
2. Binary Search (recursive, decrease and conquer)
3. Hash Table Lookup (space-time trade-off)

**Analysis Done:** Basic operation, time complexity, best/average/worst case, asymptotic notation, recurrence relation and its solution.

**Files:**
- `Problem.pdf`: problem statement
- `Solution.pdf`: concise answers to the tasks
- `Python_Code.py`: implementation and testing code
- `Report.pdf`: full report

**How to Run:**
```
pip install matplotlib
python Python_Code.py
```

**Result:** Successfully implemented and tested all three algorithms on datasets of 1K, 10K, 100K and 1M records.
- Linear search grows with n and becomes slow at 1M records.
- Binary search needs only about 20 comparisons at 1M records.
- Hash lookup needs about 1 comparison on average.
- Final design: binary search on a sorted array. For the Day-4 case (50,000 searches per hour), a hash index is added on top of it.
