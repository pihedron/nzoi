# Problem

Zombies are taking over Byteland! Driven by a desire for human brains, they are attracted to Byteland's Main Street, whose inhabitants are all programmers and thus naturally have the largest brains. Steve, as the chair of the NZIC (National Zombie Intervention Council), has decided to enact a policy of social distancing to spread out the population of Main Street and stop the spread of zombies.

Main Street consists of a row of $N$ houses, numbered from $1$ to $N$ starting from the leftmost house. Each house is spaced $X$ meters away from its neighbors. There are also $M$ programmers, each originally staying at the $h_j$-th house. As programmers never leave their houses, Steve only needs to prevent zombies from attacking programmers staying in the same house. He has determined each house to be able to safely hold a maximum of $k_i$ occupants before it begins to attract zombies. Each of the $m$ programmers must therefore be assigned a (possibly different) house to move to, such that the $i$-th house has at most $k_i$ occupants assigned to it. However, to reduce the amount of non-essential travel, each programmer can only be assigned to a house within $d_j$ meters of their original house.

As the NZIC's newest ~~code monkey~~ junior developer, you have been tasked with writing a program that finds such an arrangement (if possible). Work quickly, as the future of Byteland depends on you!

## Input
The first line of input will contain the three integers $N$, $X$ and $M$.

Following will be $N$ lines, each describing a different house on Main Street. The $i$-th such line will contain a single integer $k_i$, indicating that the $i$-th house can safely isolate at most $k_i$ occupants.

Following will be $M$ lines, each describing a different programmer. The $j$-th such line will contain two integers $h_j$ and $d_j$, indicating that the $j$-th programmer originally lived at the $h_j$-th house and can travel at most $d_j$ meters away from that house (in either direction).

## Output
If there exists a valid assignment of all programmers to houses, output `SOLUTION IS TRIVIAL``. Following this, output M lines, with the $j$-th line denoting the number of the house which the $j$-th programmer moves to. If there are multiple valid assignments, output any.

If there does not exist a valid assignment, only output the string `SOLUTION IS NON-TRIVIAL``.

## Constraints
For all subtasks:

$1\le N,M\le 50,000$

$1\le X\le 10,000$

$0\le ki\le 50,000$ for all $i$

$1\le hj\le N$ for all $j$

$0\le dj\le 500,000,000$ for all $j$

## Subtasks
Additional constraints may apply to subtasks:

Subtask 1 (13%): There are at most 2 houses with non-zero occupant limits ($k_i>0$). In other words, there are at most two houses which all programmers must move to.

Subtask 2 (12%): $N,M\le 6$

Subtask 3 (31%): $d_j<2X$ for all $j$

Subtask 4 (25%): $N\le 1000$

Subtask 5 (19%): No further constraints

Subtasks are not necessarily in difficulty order.

## Sample Explanations
Note that sample 1 fits within the constraints of subtasks 2, 4, and 5 and sample 2 fits within the constraints of subtasks 1, 2, 4, and 5.

### Sample 1
There are 3 houses each spaced 3 metres apart and 3 programmers in total. In this case, house 1 originally has two programmers (one that can travel up to 4 metres and one that can travel up to 6 metres) while house 2 originally has one programmer which can travel up to 3 metres. One valid assignment is to move the 1st programmer to house 2, move the 2nd programmer to house 3 and move the 3rd programmer to house 3.

### Sample 2
There are 6 houses spaced 100 metres apart, with the 1st and the 6th capable of holding up to 2 programmers each safely. There are 4 programmers. There does not exist a valid assignment of programmers to houses.

## Note on evaluation
Submissions which fail to follow the output format, assign a programmer farther than permitted or over-occupy a house will receive a Wrong Answer verdict in evaluation.

## Sample Input 1
```
3 3 3
0
1
2
1 4
1 6
2 3
```
## Sample Output 1
```
SOLUTION IS TRIVIAL
2
3
3
```
## Sample Input 2
```
6 100 4
2
0
0
0
0
2
3 244
4 299
6 33
5 111
```
## Sample Output 2
```
SOLUTION IS NON-TRIVIAL
```