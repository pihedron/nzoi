# Problem

Betty is a very peculiar cat, who likes to spend her days basking in sunny spots, but has some particular rules about which spots to choose.

She divides her day into $P$ ($1 \leq P \leq 1000000$) basking periods. Every morning she checks the weather forecast and determines the optimal sunny spot for each basking period throughout the day. Each basking period is thus assigned a value $V_i$, ($0 \leq V_i \leq 1000$ for $1 \leq i \leq P$)

She then wishes to select some subset of those basking periods to maximise the total value, subject to the following constraint: to prevent dehydration, she must not bask for any four consecutive basking periods.

For example, suppose she divides her day into $9$ basking periods with values $6$,$7$,$5$,$4$,$8$,$9$,$4$,$6$,$7$ in order. Selecting the basking periods:
```
6 7 5 4 8 9 4 6 7
* * *   * * * * *
```
would result in dehydration, and so is invalid, due to the five consecutive basking periods at the end. The correct solution for this input can be seen to be, giving a total of $48$:
```
6 7 5 4 8 9 4 6 7
* * *   * *   * *
```
Help Betty to find the maximum total value of basking she can attain, without becoming dehydrated.

## Input
The first line of input will consist of a single integer $P$, the number of basking periods.

The second line of input will contain $P$ integers $V_i$, each describing the value of the $i$th basking period.

## Output
Output a single line containing a single integer - the maximum total value of basking that Betty can attain.

## Subtasks
The following subtasks are available:

- Subtask 1 (20%): 0 \leq V_i \leq 1
- Subtask 2 (40%): P \leq 20
- Subtask 3 (40%): No further restrictions

## Sample Input 1
```
9
6 7 5 4 8 9 4 6 7
```
## Sample Output 1
```
48
```
## Sample Input 2
```
20
1 1 1 1 1 1 0 1 1 0 0 0 0 1 1 0 1 1 1 1
```
## Sample Output 2
```
12
```

# Solution

This is a dynamic programming problem. At the $i$th basking period, Betty has the choice of either ignoring it or selecting it unless she has selected the previous $3$ basking periods.

Specifically, we want to track the maximum basking value for not selecting the current period and the maximum basking value for selecting the previous $1$, $2$, or $3$ for each $i$.

```cpp
 6   7
[0] [6]  // max excluding V[i]
[6] [7]  // selecting V[i] but not V[i - 1]
[6] [13] // selecting V[i], V[i - 1] but not V[i - 2]
[6] [13] // selecting V[i], V[i - 1], V[i - 2]
```

We can create a `dp` table with size $P \times 4$. Then, set `dp[i][0]` to the maximum of `dp[i - 1]` and perform addition across the diagonals.