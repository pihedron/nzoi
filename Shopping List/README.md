# Problem

Ah, it's shopping day! You have N food items you want to buy and how much of each item you want, $W$.

Unfortunately, your favourite supermarkets, Countup, and PAK'nSPEND, both have a limited amount of each food item in stock, $A$ and $B$ respectively. Each supermarket has their own price for each item $X$, and $Y$, respectively.

You need to figure out the minimum cost to buy all the food you want.

## Input
The first line contains the integer N, the number of food items you want.
The next N lines each contain five space-separated integers, $W$, the amount of that item you want, $A$ and $X$, the amount and cost at Countup, and $B$ and $Y$, the amount and cost at PAK'nSPEND.
You may assume that $W\le A+B$ which means there will always be enough in stock to satisfy your shopping needs.
## Output
Output a single integer – the minimum cost to buy all your food.

## Constraints
- $1\le N\le 100$
- $1\le W\le 100$
- $0\le A,B\le 100$
- $0\le X,Y\le 100$

## Subtasks
- Subtask 1 (30%): $X=Y$ for all items
- Subtask 2 (30%): $A=B=100$ for all items
- Subtask 3 (40%): No further constraints apply

## Sample Input 1
```
1
8 5 10 6 10
```
## Sample Output 1
```
80
```
## Sample Input 2
```
2
1 100 3 100 4
1 100 5 100 4
```
## Sample Output 2
```
7
``` 
## Sample Input 3
```
1
4 2 3 100 5
```
## Sample Output 3
```
16
```