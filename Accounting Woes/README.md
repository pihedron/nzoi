# Problem

You have been given the role of treasurer in the prestigious Natural Zillionaire's Iceboat Cabal (NZIC). In this role, you oversee $N$ distinct branches of the Cabal, each of which has spent some amount of money this year to promote iceboats.

If the $N$ branches don't have the same total expense over the year, an internal fight might break out. Hence, you have been secretly tasked with manipulating the records to balance the expenses across the branches.

To ensure the total expenditure of the entire Cabal remains the same, you are allowed to subtract some integer amount from the expense of a branch and add it to the expense another branch as many times as necessary. If it is not possible to perfectly balance across the branches, you may ask some of the branches to spend more, but this amount should be minimised. You need to report the total extra spending necessary.

## Input
The first line contains a single integer, $N$ (2≤N≤100).

The second line contains $N$ space-separated integers between $0$ and $1000$ (inclusive), each representing the expense of one branch of the Cabal.

## Output
Print a single integer - the minimum total extra spending needed to ensure the expenses across the branches balance.

## Subtasks
For 50% of the marks, $N=2$
## Explanation
In sample case 1, we have three branches which have expended 10, 2, and 4 dollars. One optimal way to balance the branches is to subtract 4 from the first branch and add it to the second branch to get 6 6 4. Then we ask the third branch to spend 2 dollars more - getting a perfect balance of 6 6 6. So overall, the total extra spending is 2.

## Sample Input 1
```
3
10 2 4
```
## Sample Output 1
```
2
```

# Solution

This is probably the easiest problem on NZOI because it can be solved in `O(1)` time with mathematics. The idea is to find the **lowest** possible **multiple** of $N$ that is **greater** than the sum of all the money spent by the branches. The solution is similar to the implementation of the *modulo* operator, except we have to take the ceiling of (round up) the result instead of taking the floor (rounding down).

```py
import math

N = int(input())
nums = list(map(int, input().split()))

print(math.ceil(sum(nums) / len(nums)) * len(nums) - sum(nums))
```

```
10 + 2 + 4 = 16
16 / 3 ~ 18
18 - 16 = 2
```