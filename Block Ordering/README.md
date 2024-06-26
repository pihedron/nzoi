# Problem

Bjarne has a collection of wooden blocks numbered from 1 to $N$ and likes to play a game with them. He starts by lining all the blocks up in order. Then he assigns each block one of four rules:

 - Acquire - No block after this one can be moved before this one
 - Release - No block before this one can be moved after this one
 - Sequential - The same as 'Acquire' and 'Release' combined (which means no block after this one can be moved before this one and vice versa)
 - Relaxed - No constraints

Additionally, you are guaranteed that there will be at least one 'Sequential' block within every eight consecutive blocks. If the total number of blocks is less than eight, then there might not be any 'Sequential' block.

Given the rules for each block, Bjarne wants to know how many ways there are to order all the blocks while satisfying each rule.

## Input
The first line contains one integer, $N$, the number of blocks Bjarne has. The following $N$ lines each contain one of four possible characters:

 - 'a' if this block has the rule 'Acquire'
 - 'r' if this block has the rule 'Release'
 - 's' if this block has the rule 'Sequential'
 - 'o' if this block has the rule 'Relaxed'

## Output
Output the number of ways to order all the blocks while satisfying each rule. As the result can be a very large number, print out the number of ways modulo $10^9+7$ (the remainder of dividing by $10^9+7$).

## Constraints
For all subtasks:
 - $1\le N\le 1,000$

## Subtasks
 - Subtask 1 (+10%): $1\le N\le 7$ and every block is 'o' (Relaxed)
 - Subtask 2 (+30%): $1\le N\le 10$
 - Subtask 3 (+30%): Every block is either 'o' (Relaxed) or 's' (Sequential)
 - Subtask 4 (+30%): No further constraints

## Explanation
In the first sample case there are 2 possible block orderings:

- 1 (s), 2 (o), 3 (a), 4 (r)
- 1 (s), 3 (a), 2 (o), 4 (r)

In the second sample case there are 6 possible block orderings:

- 1 (r), 2 (o), 3 (a), 4 (r)
- 2 (o), 1 (r), 3 (a), 4 (r)
- 2 (o), 3 (a), 1 (r), 4 (r)
- 3 (a), 2 (o), 1 (r), 4 (r)
- 1 (r), 3 (a), 2 (o), 4 (r)
- 3 (a), 1 (r), 2 (o), 4 (r)

***Note:*** *Python submissions should use Python 3.6 (PyPy 7.3), as submissions using Python 3.8 may not be fast enough to pass some subtasks.*

## Sample Input 1
```
4
s
o
a
r
```
## Sample Output 1
```
2
```
## Sample Input 2
```
4
r
o
a
r
```
## Sample Output 2
```
6
```

# Solution

This problem can be solved using formulas for permutations. The 1st subtask can be solved using a standard library function.

```py
import math

N = int(input())

for _ in range(N):
    block = input()

print(math.factorial(N))
```

The 2nd subtask is just as easy since 'Sequential' blocks can't move and act as dividers. Using knowledge from probability and statistics, we can quickly solve this subtask by dividing the blocks into chunks and taking the product of the number of permutations for each chunk.

```py
import math

N = int(input())

chunks = []
chunk = 0

for _ in range(N):
    block = input()
    if block == "o":
        chunk += 1
    elif block == "a":
        pass
    elif block == "r":
        pass
    else: # block == "s"
        chunks.append(chunk)
        chunk = 0

chunks.append(chunk)

def solve_chunk():
    pass

permutations = 1

for c in chunks:
    permutations *= math.factorial(c)

print(permutations % (10 ** 9 + 7))
```