# Problem

There are number of lights along a corridor. All of the lights are off. Each light has an on-off switch.
Several people walk along the corridor, one after another.

 - The first flips every switch, turning them all on.
 - The second flips every second switch, starting from the second, turning about half of them off.
 - The third flips every third switch, starting from the third, turning some on and some off.
 - The fourth flips every fourth switch, starting from the fourth.
 - etc.

After all of the people have walked the corridor, how many switches are on?

## Input
The input will be a two lines.

The first line contains $N$, the number of lights in the corridor.

The second line contains $M$, the number of people.

## Output
Ouput the number of lights on after the M people have walked along the corridor.

## Constraints
 - $1\le M\le N$
 - $1\le N\le 1,000$
## Subtasks
 - Subtask 1 (+30%): $M=1$.
 - Subtask 2 (+30%): $M\le 2$.
 - Subtask 3 (+40%): No further constraints apply.
## Sample Input 1
```
4
2
```
## Sample Output 1
```
2
```
## Sample Input 2
```
17
1
```
## Sample Output 2
```
17
``` 
## Sample Input 3
```
17
13
```
## Sample Output 3
```
6
```

# Solution

This problem is similar to [Emma's Switches](https://train.nzoi.org.nz/problems/1311) but much easier. In this situation, a bruteforce algorithm is sufficient to pass all subtests. The switches can be represented using an array of booleans, but integers are better for counting the total number of switches that are on. 

```py
s = [0 for _ in range(N)]
```

After reading in $N$ and $M$, we have to use a nested loop to iterate from $1$ to $M$. It is important to be aware that most programming languages use 0 as the first index and that `range(M)` starts at $0$ and stops before $M$. This means we have to offset the **step** for the `range` function when we iterate over some of the switches inside the loop.

```py
for m in range(M):
    for n in range(m, N, m + 1): # when m = 0 step = 1
        s[n] += 1
        s[n] %= 2
```

The `s[n] %= 2` ensures that all the values in the array are either 0 or 1.

We can use the `sum` function to count the number of switches that are on in the array.

```py
print(sum(s))
```

The time complexity of this algorithm is $O(N^2)$.